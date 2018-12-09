from common import direct3x
import config

env='prod'
serv = direct3x.login(*config.get_direct3x_account(env), env)
