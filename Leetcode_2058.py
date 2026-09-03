# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def display_nodes(head: ListNode) -> List[ListNode]:
        node = head
        print(f"Head value {node.val}")
        while node.next != None:
            node = node.next
            print(f"Node value {node.val}")


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_pt = 0
        left = head
        dist = list()
        node_len = 1
        if left.next == None:
            return [-1, -1]
        curr = left.next
        node_len = 2
        while curr.next != None:
            right = curr.next
            if curr.val < left.val and curr.val < right.val:
                print(f"Possible critical pt - {curr.val}")
                dist.append(node_len)
                critical_pt += 1
            elif curr.val > left.val and curr.val > right.val:
                print(f"Possible critical pt - {curr.val}")
                dist.append(node_len)
                critical_pt += 1
            else:
                print("No match for critical pt")
            left = left.next
            curr = curr.next
            node_len += 1
        
        if critical_pt < 2:
            return [-1, -1] 
        
        dist.sort(reverse = True)
        min_sub = list()
        print(f"Distance vector - {dist}")
        for i in range(0, len(dist)-1):
            min_sub.append(dist[i] - dist[i+1])
        return [min(min_sub), dist[0]-dist[-1]]


def main():
    entries = [2,3,3,2]
    head = ListNode(entries[0])
    tmp_obj = head
    for entry in entries[1:]:
        node = ListNode(entry)
        tmp_obj.next = node
        tmp_obj = node

    ListNode.display_nodes(head)
    crit_pt = Solution()
    print(crit_pt.nodesBetweenCriticalPoints(head))

if __name__ == "__main__":
    main()