import csv
import pprint

from collections import Counter, OrderedDict

def get_num_correct_stats(correct_file:str, result_file: str):
    correct_emails = []
    hunter_emails = []
    snov_emails = []
    anymail_emails = []
    findemails_emails = []
    gardener_emails = []
    with open(correct_file, 'r') as r:
        fieldnames = ['domain', 'first_name', 'last_name', 'email']
        reader = csv.DictReader(r, fieldnames=fieldnames)
        header = next(reader)
        for row in reader:
            correct_emails.append(row['email'])
    
    with open(result_file, 'r') as r:
        fieldnames = ['domain', 'first_name', 'last_name', 'gardener_result', 'hunter_result', 'snov_result', 'anymail_result', 'findemails_result']
        reader = csv.DictReader(r, fieldnames=fieldnames)
        header = next(reader)
        for row in reader:
            hunter_emails.append(row['hunter_result'])
            snov_emails.append(row['snov_result'])
            anymail_emails.append(row['anymail_result'])
            findemails_emails.append(row['findemails_result'])
            gardener_emails.append(row['gardener_result'])
    
    hunter_correct = [value == correct_emails[i] for i, value in enumerate(hunter_emails)]
    snov_correct = [value == correct_emails[i] for i, value in enumerate(snov_emails)]
    anymail_correct = [value == correct_emails[i] for i, value in enumerate(anymail_emails)]
    findemails_correct = [value == correct_emails[i] for i, value in enumerate(findemails_emails)]
    gardener_correct = [value == correct_emails[i] for i, value in enumerate(gardener_emails)]

    return {
        'hunter': Counter(hunter_correct),
        'snov': Counter(snov_correct),
        'anymail': Counter(anymail_correct),
        'findemails': Counter(findemails_correct),
        'gardener': Counter(gardener_correct),
    }

def get_count_stats(result_file: str):
    fieldnames = ['domain', 'first_name', 'last_name', 'gardener_result', 'hunter_result', 'snov_result', 'anymail_result', 'findemails_result']
    stats = {
        'total_searched': 0,
        'gardener': 0,
        'hunter': 0,
        'snov': 0,
        'anymail': 0,
        'findemails': 0,
    }
    with open(result_file, 'r') as r:
        reader = csv.DictReader(r, fieldnames=fieldnames)
        header = next(reader)
        for row in reader:
            stats['total_searched'] += 1
            if row['gardener_result']:
                stats['gardener'] += 1
            if row['hunter_result']:
                stats['hunter'] += 1
            if row['snov_result']:
                stats['snov'] += 1
            if row['anymail_result']:
                stats['anymail'] += 1
            if row['findemails_result']:
                stats['findemails'] += 1
    
    return stats

if __name__ == "__main__":
    infile = input('Enter the result file of find_emails.py : ')
    correct_file = input('Enter the correct file: ')
    count_stats = get_count_stats(infile)
    acc_stats = get_num_correct_stats(correct_file, infile)
    stats = OrderedDict({
        'searched': count_stats['total_searched'],
        'hunter': {
            'found': count_stats['hunter'],
            'correct': acc_stats['hunter'][True]
        },
        'gardener': {
            'found': count_stats['gardener'],
            'correct': acc_stats['gardener'][True]
        },
        'snov': {
            'found': count_stats['snov'],
            'correct': acc_stats['snov'][True]
        },
        'findemails': {
            'found': count_stats['findemails'],
            'correct': acc_stats['findemails'][True]
        },
        'anymail': {
            'found': count_stats['anymail'],
            'correct': acc_stats['anymail'][True]
        }

    })
    pprint.pprint(stats)