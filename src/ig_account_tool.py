from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api.utils import gen_user_breadcrumb

def get_followed_accounts(username, password):
    # Log in to the Instagram account
    api = Client(username, password)
    
    # Get the user ID of the authenticated user
    user_id = api.authenticated_user_id
    
    # Generate a rank token for pagination
    rank_token = Client.generate_uuid()

    # Fetch the list of followed accounts
    followed_accounts = []
    next_max_id = ''
    
    while True:
        following = api.user_following(user_id, rank_token=rank_token, max_id=next_max_id)
        followed_accounts.extend([user['username'] for user in following['users']])
        
        # Check if there are more pages of followed accounts
        next_max_id = following.get('next_max_id')
        if not next_max_id:
            break

    return followed_accounts

# Replace 'your_username' and 'your_password' with your first account's credentials
username = 'luis.30319'
password = 'IGPass_2024'
followed_accounts = get_followed_accounts(username, password)

# Save the followed accounts to a file (optional)
with open('followed_accounts.txt', 'w') as f:
    for account in followed_accounts:
        f.write(account + '\n')

print("Followed accounts have been saved to 'followed_accounts.txt'")
