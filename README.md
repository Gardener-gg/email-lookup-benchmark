# Email Finder Benchmark

There are dozens of Email Lookup API's with little distinguish features. To help you chose we wrote a small benchmark script that tests top providers against known good and known bad emails. Our input list was sampled from Banking and IT in Europe. 

If you have another input list you would like to have tested or you would like us to add another provider just post it under our issues. 

Accuracy is calculated from total searched emails

| Service | Email Searched | Emails Found | Correct Email Found |
|---------|----------------|--------------|----------|
|[Email Gardener](https://gardener.gg) | 385 | 330 | 123 |
|[Hunter](https://hunter.io) | 385 | 96 | 66 |
|[Anymailfinder](https://anymailfinder.com) | 385 | 58 | 51 |
|[Snov](https://snov.io) | 385 | 85 | 49 |
|[Findemails](https://findemails.com)| 385 | 303 | 67 |

Numbers are hard to believe if you have not calculated them yourself, we agree and hence included the simple script in the repo. For privacy reasons we did not include our input dataset of names but we expect similar results if you simply validate with your existing known true list. 


## How to run this benchmark?

1. Clone the repository with 
    ```
    git clone https://github.com/Gardener-gg/email-lookup-benchmark.git
    ```

2. Move to project directory
    ```
    cd analytics/
    ```

3. Install dependencies with
    ```
    pip install -r requirements.txt
    ```

4. Run `find_emails.py`
    ```
    python3 find_emails.py
    ```
You will need to provide access tokens for [Email Gardener](https://gardener.gg), [Hunter](https://hunter.io), [Snov](https://snov.io) and [Anymailfinder](https://anymailfinder.com).

You will also need to provide the input csv file containing `domain`, `first_name`, `last_name` and `email`(for accuracy) for individuals in that particular order.


## Qualitative Email Lookup API comparison

### Hunter
#### Pros
- Amount of data retured is more.
- Result accuracy is decent.
#### Cons
- No metered billing
- Unused credits are not rolled over to next month
#### Sample JSON output for email finder
```json
{
  "data": {
    "first_name": "Dustin",
    "last_name": "Moskovitz",
    "email": "dustin@asana.com",
    "score": 72,
    "domain": "asana.com",
    "position": "CEO",
    "twitter": "moskov",
    "linkedin_url": "https://www.linkedin.com/in/dmoskov",
    "phone_number": null,
    "company": "Asana",
    "sources": [
      {
        "domain": "blog.asana.com",
        "uri": "http://blog.asana.com",
        "extracted_on": "2015-09-27",
        "last_seen_on": "2017-09-01",
        "still_on_page": true
      },
      ...
    ]
  },
  "meta": {
    "params": {
      "first_name": "Dustin",
      "last_name": "Moskovitz",
      "full_name": null,
      "domain": "asana.com",
      "company": null
    }
  }
}
```

### Anymailfinder
#### Pros
- Lets monthly allowance to roll over if you do not use it.
- Claims to not charge for pattern matched emails
#### Cons
- No metered billing
#### Sample JSON output for email finder
```json
{
  "email": "jsmith@acme.com",
  "email_class": "verified",
  "alternatives": [
    "john@acme.com",
    "smithj@acme.com"
  ],
  "input": {
    "full_name": "John Smith",
    "company_name": "Acme Inc"
  },
  "domain": "acme.com",
  "status": "success"
}
```

### Snov
#### Pros
- Has a nice modern feel and is planning on growing into your single source for all email marketing needs
- Credit based payment scheme and don't push too hard into setting up recurring payments
#### Cons
- Generated token expires in 1 hr so you have to refresh it everytime
- No metered billing
- Unused credits are not rolled over to next month
#### Sample Json output for email finder
```json
{
    "params":{
        "firstName":"gavin",
        "lastName":"vanrooyen",
        "domain":"octagon.com"
    },
    "data":{
        "firstName":"gavin",
        "lastName":"vanrooyen",
        "emails":[
            {
            "email":"Gavin@octagon.com",
            "emailStatus":"valid"
            }
        ]
    },
    "status":{
        "identifier":"complete",
        "description":"Emails search is completed"
    }
}
```

### FindEmails (formerly Toofr)
#### Pros
- Metered billing
#### Cons
- Have monthly subscription on top of metered billing.
- Output is very different from other providers
- Mostly pattern matched emails
- Extra effort by developer is required to go through all emails returned and decide which email is good enough.
- Having breaking changes in their API output without any versioning. Definitely not desirable if you are using automated scripts in production with FindEmails API.
### Sample Json output for email finder
Following is a sample of Json output returned by FindEmails which is different from the 
output in their docs
```json
{
    "ryan@toofr.com": {
        "confidence": 100,
        "state": "high",
        "email": "ryan@toofr.com",
        "detail": [
            {"description": "Mailserver score", "response": "+40"}, 
            {"description": "Pattern score", "response": "+27"}, 
            {"description": "MX records score", "response": "+10"}, 
            {"description": "Catchall score", "response": "+10"}, 
            {"description": "Uniqueness score", "response": "+2"}, 
            {"description": "List score", "response": "+2"}, 
            {"description": "Name score", "response": "+2"}, 
            {"description": "Disposable score", "response": "+2"}, 
            {"description": "Gibberish score", "response": "+2"}
        ],
    },
    ...
    "employee": {
        "first_name": "ryan",
        "last_name": "buckley",
        "title": "founder",
        "profile": {
            "fn":"Ryan Buckley",
            "photo":"https://media.licdn.com/dms/image/C4D03AQFIi292VtKikw/profile-displayphoto-shrink_200_200/0?e=1536192000&v=beta&t=aXWOwRlu17VF_r96euIeWvX00I8OYfOrwhaK-Xbmksg",
            "title":"Builder of ToOfr, Inlistio, and Voxloca. Author of The Parallel Entrepreneur. Resident of Contra Costa County.",
            "linkedin_profile":"https://www.linkedin.com/in/rbuckley"
        },
            "email": {
              "email": "ryan@toofr.com",
              "confidence": 70,
              "state": "high"
        }
    }
} 
```

### Gardener
#### Pros
- Developer oriented API only service
- True metered billing with no monthly cap or minimum monthly charge.
- 0 API call = $0 bill
#### Cons
- New in competition
- No free plan
#### Sample Json output for email finder
```json
{
  "emails": [
    {
      "first_name": "John",
      "last_name": "Wick",
      "email": "john.wick@example.com",
      "source_uri": ""
    }
  ],
  "email_count": 1,
  "company": "Example"
}
```
