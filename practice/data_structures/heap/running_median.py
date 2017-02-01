#https://www.hackerrank.com/challenges/find-the-running-median

def swap(heap, id1, id2):
    temp = heap[id1]
    heap[id1] = heap[id2]
    heap[id2] = temp

def mindownHeap(heap, i):
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

def minupHeap(heap, index):
    parent = (index - 1)//2
    while parent >= 0 and heap[parent] > heap[index]:
        swap(heap, parent, index)
        index = parent
        parent = (index - 1)//2

def maxdownHeap(heap, i):
    left = i * 2 + 1
    right = i * 2 + 2
    while right < len(heap):
        if heap [i] < heap[left] and heap[i] < heap[right]:
            if heap[left] < heap[right]:
                swap(heap, i, right)
                i = right
            else:
                swap(heap, i, left)
                i = left
        elif heap[i] < heap[left]:
            swap(heap, i, left)
            i = left
        elif heap[i] < heap[right]:
            swap(heap, i, right)
            i = right
        else:
            return
        left = i * 2 + 1
        right = i * 2 + 2

    if left < len(heap):
        if heap[i] < heap[left]:
            swap(heap, i, left)

def maxupHeap(heap, index):
    parent = (index - 1)//2
    while parent >= 0 and heap[parent] < heap[index]:
        swap(heap, parent, index)
        index = parent
        parent = (index - 1)//2


if __name__ == '__main__':
    size = int(input())
    minHeap = []
    maxHeap = []

    first = int(input())
    maxHeap.append(first)
    median = first
    print(str(median * 1.0))

    for i in range(1,size):
        num = int(input())
        if num < median and len(maxHeap) - len(minHeap) < 1:
            maxHeap.append(num)
            maxupHeap(maxHeap, len(maxHeap)-1)
            if (len(minHeap) + len(maxHeap))%2 == 1:
                median = maxHeap[0]
            else:
                median = (maxHeap[0] + minHeap[0])/2
        elif num < median and len(maxHeap) - len(minHeap) == 1:
            minHeap.append(maxHeap[0])
            minupHeap(minHeap, len(minHeap)-1)
            maxHeap[0] = num
            maxdownHeap(maxHeap, 0)
            median = (maxHeap[0] + minHeap[0]) / 2
        elif num > median and len(minHeap) - len(maxHeap) < 1:
            minHeap.append(num)
            minupHeap(minHeap, len(minHeap)-1)
            if (len(minHeap) + len(maxHeap))%2 == 1:
                median = minHeap[0]
            else:
                median = (maxHeap[0] + minHeap[0])/2
        elif num > median and len(minHeap) - len(maxHeap) == 1:
            maxHeap.append(minHeap[0])
            maxupHeap(maxHeap, len(maxHeap)-1)
            minHeap[0] = num
            mindownHeap(minHeap, 0)
            median = (maxHeap[0] + minHeap[0]) / 2
        else:
            if len(minHeap) == len(maxHeap):
                maxHeap.append(num)
                maxupHeap(maxHeap, len(maxHeap)-1)
                median = maxHeap[0]
            elif len(minHeap) > len(maxHeap):
                maxHeap.append(num)
                maxupHeap(maxHeap, len(maxHeap)-1)
                median = (maxHeap[0] + minHeap[0]) / 2
            else:
                minHeap.append(num)
                upminHeap(minHeap, len(minHeap)-1)
                median = (maxHeap[0] + minHeap[0]) / 2
        print(str(median * 1.0))
            
            
