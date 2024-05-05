import readline  # Importing readline module for tab autocompletion

def generate_email_addresses(names, domain, output_file):
    try:
        # Generate permutations of email addresses
        email_addresses = []
        for name in names:
            name_parts = name.split()
            first_name = name_parts[0].lower()
            last_name = name_parts[-1].lower()
            
            # Generate permutations of email addresses
            email_permutations = [
                f"{first_name}.{last_name}@{domain}",
                f"{first_name[0]}{last_name}@{domain}",
                f"{first_name}@{domain}",
                f"{last_name}@{domain}",
                f"{first_name}{last_name}@{domain}",
                f"{first_name}.{last_name[0]}@{domain}",
                f"{first_name[0]}.{last_name}@{domain}",
                f"{last_name}.{first_name}@{domain}",
                f"{last_name[0]}{first_name}@{domain}",
                f"{last_name}{first_name}@{domain}"
            ]
            email_addresses.extend(email_permutations)

        # Remove duplicates
        email_addresses = list(set(email_addresses))

        # Write the generated email addresses to the output file
        with open(output_file, 'w') as file:
            for email in email_addresses:
                file.write(email + '\n')

        print(f"Email addresses generated successfully and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

def display_help():
    print("""
    Usage: python script.py

    Generates potential email addresses based on a list of employee names.

    """)

if __name__ == "__main__":
    import sys

    # Display help menu by default
    display_help()

    try:
        # Prompt user for domain name
        domain = input("Enter the domain name (e.g., company.com): ").strip()

        # Prompt user for the path to the file containing names
        names_file = input("Enter the path to the file containing first names and last names (one per line): ").strip()

        # Read names from the file
        with open(names_file, 'r') as file:
            names = [name.strip() for name in file.readlines()]

        # Prompt user for output file name
        output_file = input("Enter the output file name: ").strip()

        generate_email_addresses(names, domain, output_file)

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)