#https://www.hackerrank.com/challenges/qheap1

#This is a min heap

#When deleting a node in the heap I think it takes O(n) time to find the item.
#After item is found swap the item with the last item in the list.
#Delete last item and reHeap the number at that index...

def swap(heap, id1, id2):
    temp = heap[id1]
    heap[id1] = heap[id2]
    heap[id2] = temp
    
def buildHeap(heap):
    for i in range(len(heap)//2-1, 0, -1):
        downHeap(heap, i)

def downHeap(heap, i):
    left = i * 2 + 1
    right = i * 2 + 2
    while right < len(heap):
        if heap [i] > heap[left] and heap[i] > heap[right]:
            if heap[left] < heap[right]:
                swap(heap, i, left)
                i = left
            else:
                swap(heap, i, right)
                i = right
        elif heap[i] > heap[left]:
            swap(heap, i, left)
            i = left
        elif heap[i] > heap[right]:
            swap(heap, i, right)
            i = right
        else:
            return
        left = i * 2 + 1
        right = i * 2 + 2

    if left < len(heap):
        if heap[i] > heap[left]:
            swap(heap, i, left)

def upHeap(heap, index):
    parent = (index - 1)//2
    while parent >= 0 and heap[parent] > heap[index]:
        swap(heap, parent, index)
        index = parent
        parent = (index - 1)//2

def reHeap(heap, index):
    parent = (index - 1)//2
    if parent >= 0 and index < len(heap) and heap[index] < heap[parent]:
        upHeap(heap, index)
    else:
        downHeap(heap, index)
        

if __name__ == '__main__':
    size = int(input())
    heap = []
    for i in range(size):
        msg = [int(temp) for temp in input().strip().split()]
        command = int(msg[0])
        if command == 1:
            num = int(msg[1])
            heap.append(num)
            upHeap(heap, len(heap)-1)
        elif command == 2:
            num = int(msg[1])
            index = heap.index(num)
            heap[index] = heap[-1]
            del heap[-1]
            reHeap(heap, index)
        else:
            print(str(heap[0]))
            
