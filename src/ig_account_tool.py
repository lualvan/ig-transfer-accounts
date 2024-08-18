from instagram_private_api import Client

def get_followed_accounts(username, password):
    api = Client(username, password)
    user_id = api.authenticated_user_id
    following = api.user_following(user_id)
    
    followed_accounts = [user['username'] for user in following['users']]
    return followed_accounts

# Replace 'your_username' and 'your_password' with your first account's credentials
username = 'luis.30019'
password = 'f11g08r92'
followed_accounts = get_followed_accounts(username, password)

# Save the followed accounts to a file (optional)
with open('followed_accounts.txt', 'w') as f:
    for account in followed_accounts:
        f.write(account + '\n')
