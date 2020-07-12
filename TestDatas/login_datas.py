# 正常场景
success_data = {'user': '13916686542', 'passwd': '520lemon'}

# 异常场景（手机号格式不正确）
phone_data = [
    {'user': '1391668654', 'passwd': '520lemon', 'check': '请输入正确的手机号'},
    {'user': '139166865422', 'passwd': '520lemon', 'check': '请输入正确的手机号'},
    {'user': '', 'passwd': '520lemon', 'check': '请输入手机号'},
    {'user': '1111668654', 'passwd': '520lemon', 'check': '请输入正确的手机号'}
]
