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

Put example json outputs for all of them

### Hunter
#### Pros
#### Cons

### Anymailfinder
#### Pros
- Lets monthly allowance to roll over if you do not use it.
- Claims to not charge for pattern matched emails
#### Cons

### Snov
#### Pros
- Has a nice modern feel and is planning on growing into your single source for all email marketing needs
- Credit based payment scheme and don't push too hard into setting up recurring payments
#### Cons
- Generated token expires in 1 hr so you have to refresh it everytime

### FindEmails (formerly Toofr)
#### Pros
- Metered billing
#### Cons
- Have monthly subscription on top of metered billing.
- Output is very different from other providers
- Mostly pattern matched emails
- Extra effort by developer is required to go through all emails returned and decide which email is good enough.
- Having breaking changes in their API output without any versioning. Definitely not desirable if you are using automated scripts in production with FindEmails API.

### Gardener
#### Pros
- Developer oriented API only service
- True metered billing with no monthly cap or minimum monthly charge.
- 0 API call = $0 bill
#### Cons 
