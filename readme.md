https://github.com/github/advisory-database.git

find ./CVE/* -type f -name "*.json" -exec mongoimport -d GHSA -c advisories {} 


goals: 

* Advanced filtering methods (negate, group etc)
* Select only specific fields instead of the entire document (ie only return summary)
* Merge duplicate GHSA records (some advisories are older than others but they have the same id, we need to find a way to merge them into a single record without loosing the history of the changes from each of them)



```
To get the index name or the index specification document for the 
db.collection.dropIndex()
 method, use the db.collection.getIndexes() method.

The 
db.collection.dropIndex()
 method takes the following parameter:

```


```
db.advisories.find({
  "affected.package.ecosystem": "Go",
  "database_specific.cwe_ids": "CWE-78"
})


  _id: ObjectId("6439b6e7820faefc14e26e23"),
    schema_version: '1.4.0',
    id: 'GHSA-3v3c-r5v2-68ph',
    modified: '2023-01-20T22:07:25Z',
    published: '2017-11-30T23:14:55Z',
    aliases: [ 'CVE-2017-0909' ],
    summary: 'private_address_check contains Incomplete List of Disallowed Inputs',
    details: 'The private_address_check ruby gem before 0.4.1 is vulnerable to a bypass due to an incomplete blacklist of common private/local network addresses used to prevent server-side request forgery.',
    severity: [],
    affected: [
      {
        package: { ecosystem: 'RubyGems', name: 'private_address_check' },
        ranges: [ { type: 'ECOSYSTEM', events: [ [Object], [Object] ] } ]
      }
    ],
    references: [
      {
        type: '{ADVISORY}',
        url: 'https://nvd.nist.gov/vuln/detail/CVE-2017-0909'
      },
      {
        type: 'WEB',
        url: 'https://github.com/jtdowney/private_address_check/pull/3'
      },
      { type: 'WEB', url: 'https://hackerone.com/reports/288950' },
      {
        type: 'ADVISORY',
        url: 'https://github.com/advisories/GHSA-3v3c-r5v2-68ph'
      },
      {
        type: 'PACKAGE',
        url: 'https://github.com/jtdowney/private_address_check'
      }
    ],
    database_specific: {
      cwe_ids: [ 'CWE-184' ],
      severity: 'HIGH',
      github_reviewed: true,
      github_reviewed_at: '2020-06-16T20:56:20Z',
      nvd_published_at: null
    }
  }
]

```




`db.advisories.find({"done.type:": "CVSS_V3"})`


```
db.advisories.find({
  "affected.package.ecosystem": "Go",
  "database_specific.aliases:": "CVE-2022-29583"
})
```


```
db.advisories.distinct("affected.package.ecosystem")
```