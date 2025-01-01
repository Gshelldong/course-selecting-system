import os

# 项目的基本路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 项目的数据存放路径
DATA_PATH = os.path.join(BASE_PATH,'db','data')

# 日志目录
LOG_DIR = os.path.join(BASE_PATH,'log')


# 定义三种日志输出格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'


# 定义日志输出格式 结束
"""
下面的两个变量对应的值 需要你手动修改
"""
logfile_dir = LOG_DIR  # log文件的目录
logfile_name = 'business.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)
# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},  # 过滤日志
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集debug及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*50,  # 日志大小 50M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        # 这里为空的话在个体logger的时候可以随意定义logger的名字
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },  # 当键不存在的情况下 默认都会使用该k:v配置
    },
}

# 使用日志字典配置
# logging.config.dictConfig(LOGGING_DIC)  # 自动加载字典中的配置
# logger1 = logging.getLogger('log dict')
# logger1.debug('logging DEBUG!')