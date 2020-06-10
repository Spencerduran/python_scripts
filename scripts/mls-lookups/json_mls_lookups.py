
const FS = require('fs');

const META   = JSON.parse(FS.readFileSync(process.argv[2]));
let RESOURCE = process.argv[3];
let FIELD    = process.argv[4];
const FLAG   = process.argv[5];

let by_desc = false;

if (RESOURCE && RESOURCE === '--d') {
  by_desc = true;
  RESOURCE = FIELD;
  FIELD = FLAG;
}

const CLASSES = META.Classes.filter(x => x.Resource === RESOURCE);

let long_name;
let system_name;
let lookups = {};

for (let cls of CLASSES) {
  if (!by_desc) {
    if (cls.metadata[FIELD]) {
      long_name = cls.metadata[FIELD].LongName;
      
      if (META.Lookups[RESOURCE][cls.metadata[FIELD].LookupName]) {
        for (let lookup of META.Lookups[RESOURCE][cls.metadata[FIELD].LookupName].metadata.map(x => x.LongValue)) {
          lookups[lookup] = true;
        }
      }

      break;
    }
  } else {
    for (let field in cls.metadata) {
      if (cls.metadata[field].LongName === FIELD) {
        if (META.Lookups[RESOURCE][cls.metadata[field].LookupName]) {
          for (let lookup of META.Lookups[RESOURCE][cls.metadata[field].LookupName].metadata.map(x => x.LongValue)) {
            lookups[lookup] = true;
          }
        }
      }
    }
  }
}

for (let cls of CLASSES) {
  let lookup_sets = Object.keys(cls.metadata)
                        .filter(x => cls.metadata[x].LongName === long_name)
                        .map(x => cls.metadata[x].LookupName)
                        .filter(x => META.Lookups[RESOURCE][x] != null)
                        .map(x => META.Lookups[RESOURCE][x].metadata)
                        .filter(x => x != null);

  for (let lookup_set of lookup_sets) {
    for (let lookup of lookup_set.map(x => x.LongValue)) {
      lookups[lookup] = true;
    }
  }
}

console.log(`-----------------------------Desc----------------------------`);

for (let key in lookups) {
  let suffix = `${ key.indexOf('.') != -1 ? '             <= ********' : '' }`;

  console.log(`   ${ key }${ suffix }`);
}

if (by_desc) {
  process.exit(0);
}

///
///
///
///

let desc_lookups = Object.assign({}, lookups);

lookups = {};

for (let cls of CLASSES) {
  if (cls.metadata[FIELD]) {
    system_name = cls.metadata[FIELD].SystemName;
    
    if (META.Lookups[RESOURCE][cls.metadata[FIELD].LookupName]) {
      for (let lookup of META.Lookups[RESOURCE][cls.metadata[FIELD].LookupName].metadata.map(x => x.LongValue)) {
        lookups[lookup] = true;
      }
    }

    break;
  }
}

for (let cls of CLASSES) {
  let lookup_sets = Object.keys(cls.metadata)
                        .filter(x => cls.metadata[x].SystemName === system_name)
                        .map(x => cls.metadata[x].LookupName)
                        .filter(x => META.Lookups[RESOURCE][x] != null)
                        .map(x => META.Lookups[RESOURCE][x].metadata)
                        .filter(x => x != null);

  for (let lookup_set of lookup_sets) {
    for (let lookup of lookup_set.map(x => x.LongValue)) {
      lookups[lookup] = true;
    }
  }
}

console.log(`-----------------------------+Field---------------------------`);

for (let key in lookups) {
  let suffix = `${ key.indexOf('.') != -1 ? '             <= ********' : '' }`;

  console.log(`   ${ key }${ suffix }`);
}

console.log(`--------------------------------------------------------------`);

process.exit(0);
