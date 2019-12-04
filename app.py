from thread import thread


if __name__ == '__main__':
    rpc = thread.Rpc("")
    t = thread.TestCall("")

    rpc.start()
    t.start()

