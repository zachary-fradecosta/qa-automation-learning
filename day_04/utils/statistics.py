from utils.user_helpers import get_active_users, get_users_by_role

def get_user_statistics(users):
    total_count = len(users)
    active_count = len(get_active_users(users))
    locked_count = total_count - active_count
    admin_count = len(get_users_by_role(users, "admin"))
    customer_count = len(get_users_by_role(users, "customer"))

    return {
        "total": total_count,
        "active": active_count,
        "locked": locked_count,
        "admins": admin_count,
        "customers": customer_count
    }