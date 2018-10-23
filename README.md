# Gardener Email Finder Benchmark

We ran multiple email lookup services to find emails. Here are the 
statistics from our run.

Accuracy is calculated from total searched emails

| Service | Email Searched | Emails Found | Accuracy |
|---------|----------------|--------------|----------|
|[Email Gardener](https://gardener.gg) | 25 | 24 | 20% |
|[Hunter](https://hunter.io) | 25 | 22 | 70% |
|[Snov](https://snov.io) | 25 | 2 | 8% |
|[Anymailfinder](https://anymailfinder.com) | 25 | 14 | 52% |

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