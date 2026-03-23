class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.hyd_sem = threading.Semaphore(2)
        self.ox_sem = threading.Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hyd_sem.acquire()
        self.barrier.wait()
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hyd_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.ox_sem.acquire()
        self.barrier.wait()
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.ox_sem.release()