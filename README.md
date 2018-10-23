# Gardener Email Finder Benchmark

There are dozans of Email Lookup API's with little distinguish features to help you chose we wrote a small benchmark script that tests top providers against known good and known bad emails. Our input list was sampled from Banking and IT in europe. 

If you have another input list you would like to have tested or you would like us to add another provider just post it under our issues. 

Accuracy is calculated from total searched emails

| Service | Email Searched | Emails Found | Accuracy |
|---------|----------------|--------------|----------|
|[Email Gardener](https://gardener.gg) | 25 | 24 | 20% |
|[Hunter](https://hunter.io) | 25 | 22 | 70% |
|[Snov](https://snov.io) | 25 | 2 | 8% |
|[Anymailfinder](https://anymailfinder.com) | 25 | 14 | 52% |

Numbers are hard to believe if you have not calculated them yourself, we agree and hence included the simple script in the repo.  We also included our test input set of names, for privacy reasons we did not include our input dataset of names but we expect similar results if you simply validate with your existing known true list. 


## How run this benchmark?

1. Clone the repository with 
    ```
    git clone https://github.com/Gardener-gg/analytics.git
    ```

2. Move to project directory
    ```
    cd analytics/
    ```

3. Run `find_emails.py`
    ```
    python3 find_emails.py
    ```
You will need to provide access tokens for [Email Gardener](https://gardener.gg), [Hunter](https://hunter.io), [Snov](https://snov.io) and [Anymailfinder](https://anymailfinder.com).

You will also need to provide the input csv file containing `domain`, `first_name`, `last_name` and `email`(for accuracy) for individuals in that particular order.


## Qualitative Email Lookup API comparison

TODO Put example json outputs for all of them 
Hunter  : TODO
Anymailfinder : has the advantage of letting your monthly allownace roll over if you do not use it and they claim to not charge you for pattern matched emails.  
FindEmails (formerly known as toofr) : Uses metered billing but they still have a monthly subscription charge so it is not truely metered billing. Their output different from other providers in that they return to you all their guesses at possible emails with a score meaning you have to go through the json to decide which email to infact use. This output makes it clear that they are mostly just pattern matching but it puts extra effort on the developer to decide if an email returned is good enough.  Also I would note that they changed their api output without preserving the old schema which broke our code in a few weeks ago,  not something I would want in production.  
Snov : Has a nice modern feel and is planning on growing into your single source for all email marketing needs. They have a credit based payment scheme and don't push you to hard into setting up reccuring payments. 

Gardener :  developer oriented API only service with metered billing and no monthly fee.  New player in the market. 
