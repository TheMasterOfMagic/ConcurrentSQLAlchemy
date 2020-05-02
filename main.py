from multiprocessing import Pool as PPool
from multiprocessing.pool import ThreadPool as TPool
from utils import logging


PPOOL_SIZE, PROCESS_NUMBER = 2, 3
TPOOL_SIZE, THREAD_NUMBER = 2, 3


def process(i):
    def thread(j):
        from model import User
        try:
            User.get_all(i, j)
            User.add_user(i, j)
            User.get_all(i, j)
        except Exception as exc:
            logging.error(f'{i}-{j} {type(exc).__name__}:{exc.args}')
    try:
        tpool = TPool(TPOOL_SIZE)
        list(tpool.apply_async(thread, (j,)) for j in range(1, THREAD_NUMBER+1))
        tpool.close()
        tpool.join()
    except Exception as exc:
        logging.error(f'{i} {type(exc).__name__}:{exc.args}')

if __name__ == '__main__':
    ppool = PPool(PPOOL_SIZE)
    list(ppool.apply_async(process, (i,)) for i in range(1, PROCESS_NUMBER+1))
    ppool.close()
    ppool.join()
