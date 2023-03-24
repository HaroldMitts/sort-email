def sort_emails_by_domain(emails):
    return sorted(emails, key=lambda email: email.split('@')[1])

def read_emails_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def write_emails_to_file(filename, emails):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    input_filename = 'email_addresses.txt'  # Change this to the name of your input file
    output_filename = 'sorted_email_addresses.txt'  # Change this to the name of your output file

    emails = read_emails_from_file(input_filename)
    sorted_emails = sort_emails_by_domain(emails)
    write_emails_to_file(output_filename, sorted_emails)

if __name__ == '__main__':
    main()
