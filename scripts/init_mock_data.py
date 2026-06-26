import os
import sys
import django

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

def run():
    from users.models import User, Department, Role, UserDeptRole
    
    print("Creating mock data for frontend testing...")
    
    # 1. 创建部门
    dept_finance, _ = Department.objects.get_or_create(name="财务部 (Finance)", defaults={"code": "FIN"})
    dept_it, _ = Department.objects.get_or_create(name="IT部 (IT)", defaults={"code": "IT"})
    
    # 2. 创建角色
    role_acc, _ = Role.objects.get_or_create(name="会计 (Accountant)", defaults={"data_scope": "DEPARTMENT"})
    role_admin, _ = Role.objects.get_or_create(name="管理员 (Admin)", defaults={"data_scope": "ALL"})
    
    # 3. 创建测试用户
    user_zhang, _ = User.objects.get_or_create(username="zhangsan", defaults={
        "first_name": "张三 (Zhang San)", 
        "email": "zhangsan@example.com",
        "is_active": True
    })
    if _:
        user_zhang.set_password("password123")
        user_zhang.save()

    user_admin, _ = User.objects.get_or_create(username="admin", defaults={
        "first_name": "超级管理员", 
        "email": "admin@example.com",
        "is_superuser": True,
        "is_staff": True,
        "is_active": True
    })
    if _:
        user_admin.set_password("admin123")
        user_admin.save()
        
    # 4. 创建三元关联 (User - Dept - Role)
    UserDeptRole.objects.get_or_create(user=user_zhang, department=dept_finance, role=role_acc)
    UserDeptRole.objects.get_or_create(user=user_admin, department=dept_it, role=role_admin)
    
    print("Mock data created successfully!")

if __name__ == '__main__':
    run()