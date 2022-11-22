# status (delete) = 0 | 1
不加唯一索引
判断 存在 && status == 0
不考虑重复

# 修改了 requirements 
# 需要替换db
# 用pandas写了导入导出csv的模板
# sqlite的wal还是不清楚
#


core：
    dbhelper：orm和db交互的封装
    events：db开关
    exceptions：单独写的异常抛出格式，通了就是200，然后包了一层内部逻辑的异常
    log：字面意思.jpg
    middleware：目前是CORS跨域和打日志
    security：安全相关的依赖 JWT
    service：crud和分页
    utils:目前是小模块，注册路由和list2tree，以及一个随机获取数字

model：
生成db的，common有一个抽象类 生成统一的东西
五张表
user
role
control
user_role
role_control

router：
路由四大部分的增删查改
认证（登录），用户，角色，权限。

schemas：
模式？
包括orm和db沟通用的类
以及fastapi接口接受和响应的类规范

service：
各种业务封装的类