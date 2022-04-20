
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
import bcrypt
from functools import wraps


### custom wrap to determine role access  ### 
def roles_required(*role_names):
    def decorator(original_route):
        @wraps(original_route)
        def decorated_route(*args, **kwargs):
            if not current_user.is_authenticated:
                print('The user is not authenticated.')
                return 'The user is not authenticated' #redirect(url_for('main.profile'))
            print(current_user.role)
            print(role_names)
            if not current_user.role in role_names:
                print('The user does not have this role.')
                return 'The user does not have this role' #redirect(url_for('main.profile'))
            else:
                print('The user is in this role.')
                return original_route(*args, **kwargs)
        return decorated_route
    return decorator
