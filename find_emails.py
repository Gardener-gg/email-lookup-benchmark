import csv
import requests
from pyhunter import PyHunter


def gardener_email_finder(
        token: str,
        row: dict):
    """
    Finds the email from Gardener API

    return: A string of emails seperated by `:`
    """
    params = {**row}
    url = 'https://gardener.gg/api/v1/email-finder/'
    header = {
        'Authorization': 'Token {}'.format(token)
        }

    resp = requests.get(url, params=params, headers=header)
    if resp.status_code == requests.codes.ok:
        if resp.json().get('email_count', 0):
            res = resp.json()
            emails = ':'.join([email['email'] for email in res['emails']])
            return emails
        
    return None


def anymail_email_finder(
        token: str,
        row: dict):
    """
    Finds the email from Anymail Api

    Returns the email or None if not found
    """
    params = {**row}
    header = {
        'X-Api-Key': token
    }
    url = 'https://api.anymailfinder.com/v4.0/search/person.json'
    resp = requests.post(url, data=params, headers=header)
    if resp.status_code == requests.codes.ok:
        return resp.json()['email']

    return None


def snov_email_finder(
        token: str,
        row: dict):
    """
    Finds the email from Snov.io API

    return: A `:` seperated string of emails
    """
    params = {
            'access_token': token,
            'domain': row['domain'],
            'firstName': row['first_name'],
            'lastName': row['last_name'],
    }
    url = 'https://app.snov.io/restapi/get-emails-from-names'
    resp = requests.post(url, data=params)
    if resp.status_code == requests.codes.ok:
        print(resp.json())
        if not resp.json().get('errors', ''):
            if not resp.json()['status']['identifier'] == 'not_found':
                email = ':'.join([email['email'] for email in resp.json()['data']['emails']])
                return email

    return None

def toofr_email_finder(
        token: str,
        row: dict):
    params= {
        'first_name': row['first_name'],
        'last_name': row['last_name'],
        'company_name': row['domain'],
        'key': token,
    }
    url = "https://www.findemails.com/api/v1/guess_email.json"
    resp = requests.post(url, data=params)
    if resp.status_code == requests.codes.ok:
        email = resp.json()['employee']['email']['email']
        return email
    
    return None


def find_emails(
        gardener_token : str,
        hunter_token : str,
        snov_token : str,
        anymail_token: str,
        findemails_token: str,
        infile: str,
        outfile: str):
    """
    store the found emails in a csv format

    infile: A csv file with domain, first_name and last_name
    outfile: A csv file with domain, first_name, last_name, gardener_result, 
             hunter_result, snov_result and anymail_result
    """
    with open(infile, 'r') as r, open(outfile, 'w') as w:
        hunter = PyHunter(hunter_token)
        fieldnames = ['domain', 'first_name', 'last_name', 'email']
        w_fieldnames = ['domain', 'first_name', 'last_name', 'gardener_result', 'hunter_result', 'snov_result', 'anymail_result', 'findemails_result']
        reader = csv.DictReader(r, fieldnames=fieldnames)
        writer = csv.DictWriter(w, fieldnames=w_fieldnames)
        writer.writeheader()
        header = next(reader)
        for row in reader:
            del row['email']
            print(dict(row))
            write_row = {
                'gardener_result': '',
                'hunter_result': '',
                'snov_result': '',
                'anymail_result': '',
                'findemails_result': '',
                **row
            }

            # get the result from gardener
            write_row['gardener_result'] = gardener_email_finder(gardener_token, row)
            # get the result from hunter
            email, confidence = hunter.email_finder(**row)
            write_row['hunter_result'] = email
            # get the result from snov
            write_row['snov_result'] = snov_email_finder(snov_token, row)
            #  get the result from anymail
            write_row['anymail_result'] = anymail_email_finder(anymail_token, row)
            # get the toofr response
            write_row['findemails_result'] = toofr_email_finder(findemails_token, row)
            
            writer.writerow(write_row)

if __name__ == "__main__":
    gardener_token = input("Enter Gardener token: ")
    hunter_token = input("Enter Hunter token: ")
    snov_token = input("Enter Snov token: ")
    anymail_token = input("Enter Anymail token: ")
    findemails_token = input("Enter findemails token: ")
    infile = input("Enter Input Filename: ")
    outfile = input("Enter Output Filename: ")
    find_emails(gardener_token, hunter_token, snov_token, anymail_token, findemails_token, infile, outfile)
