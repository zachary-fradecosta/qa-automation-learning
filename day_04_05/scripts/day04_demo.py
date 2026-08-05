from utils.user_helpers import get_active_users, get_eligible_users, get_users_by_role, count_users
from utils.json_loader import load_users
from utils.statistics import get_user_statistics

# Exercice 3: Display active users.
users = load_users("data/users.json")

for user in get_active_users(users):
    print(f"Active user: {user['username']}")

# Exercie 4: Display eligible users.
for user in get_eligible_users(users):
    print(f"Eligible user: {user['username']}")

# Ticket QA-004: Display user counts by role.
admin_users = get_users_by_role(users, "admin")
customer_users = get_users_by_role(users, "customer")

print(f"Number of admin users: {count_users(admin_users)}")
print(f"Number of customer users: {count_users(customer_users)}")

#Challenge: Display global user statistics.
user_statistics = get_user_statistics(users)
print(user_statistics)