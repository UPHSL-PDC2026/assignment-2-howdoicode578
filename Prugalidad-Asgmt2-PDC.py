from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Master process receiving results:\n")
    for i in range(1, size):
        result = comm.recv(source=i)
        print(result)
else:
    task_chunk = list(range(rank * 10, rank * 10 + 10))
    computation = sum(task_chunk)

    message = (
        f"Process {rank} | "
        f"Task: sum of {task_chunk} | "
        f"Result: {computation}"
    )

    comm.send(message, dest=0)