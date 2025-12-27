class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_stack = [0]
        visited = set(room_stack)

        while room_stack:
            idx = room_stack.pop()
            for i in rooms[idx]:
                if i not in visited:
                    room_stack.append(i)
                    visited.add(i)
        if len(visited) == len(rooms):
            return True
        return False


        