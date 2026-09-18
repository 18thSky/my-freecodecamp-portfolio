'''
The Official Architect's Blueprint
1. The Manager (hanoi_solver(n)):

Create rod1 and fill it with numbers from n down to 1. (e.g., if n=3, it should be [3, 2, 1]).

Create rod2 and rod3 as empty lists.

Create an empty list called moves.

Take a snapshot of the starting rods (format them as strings) and append it to moves.

2. The Worker (move(disks, source, target, aux)):

Define this function directly underneath your lists, still indented inside hanoi_solver.

Base Case: If disks is greater than 0, execute the following three steps. (If it is 0, do nothing).

Step A (Recurse): Call move() to shift disks - 1 from the source rod to the aux (auxiliary/spare) rod.

Step B (The Actual Move): .pop() the last item from the source rod and .append() it to the target rod. Take a string snapshot of all three rods and append it to the moves list.

Step C (Recurse): Call move() again to shift disks - 1 from the aux rod onto the target rod.

3. The Execution (Back in hanoi_solver):

Call your move function for the first time. Give it n disks, and pass in your three rod lists (rod1 is source, rod3 is target, rod2 is aux).

Return the moves list, joined together by newline characters (\n).
'''

def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []
    moves = []

    def record_snapshot():
        moves.append(f"{rod1} {rod2} {rod3}")

    record_snapshot()

    def move(disks, source, target, aux):
        if disks > 0:
            # Step A: Move (disks - 1) from START to SPARE (using TARGET as the temp spare slot)
            move(disks - 1, source, aux, target)

            # Step B: The Actual Move (FIXED)
            disk_to_move = source.pop()
            target.append(disk_to_move)
            
            record_snapshot()

            # Step C: Move (disks - 1) from SPARE to TARGET (using START as the temp spare slot)
            move(disks - 1, aux, target, source)

    move(n, rod1, rod3, rod2)

    return "\n".join(moves)