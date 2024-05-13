class Heap {
    
    // correct min heap
    val arr = intArrayOf(2, 3, 4, 9, 11, 6, 7, 12, 10)
    
    fun push(index: Int, num: Int): Int {
        if (num == arr[index]) {
            return index
        } else if (num < arr[index]) {
            arr[index] = num
            return siftUp(index)
        } else {
            arr[index] = num
            return siftDown(index)
        }
        
    }
    
    fun print() {
        println(arr.contentToString())
    }
    
    private fun siftUp(index: Int): Int {
        var index = index // явно прописываем мутабельность
        while (arr[index] < arr[(index - 1) / 2]) {
            swapByIndex(index, (index - 1) / 2)
            index = (index - 1) / 2
        }
        
        return index
    }
    
    private fun siftDown(index: Int): Int {
        var index = index
        
        // пока есть дети
        while(2 * index + 1 < arr.size) {
            val lc = 2 * index + 1
            val rc = 2 * index + 2
            
            var lowestChildIndex = lc
            // берем наименьшего ребенка
			if (rc < arr.size && arr[rc] < arr[lc]) {
                lowestChildIndex = rc
            }
            
            // новый элемент на своем месте
            if (arr[index] <= arr[lowestChildIndex]) break
            
            swapByIndex(index, lowestChildIndex)
            
            index = lowestChildIndex
        }
        
        return index
    }
    
    private fun swapByIndex(i: Int, j: Int) {
        arr[i] = arr[j].also { arr[j] = arr[i] }
    }
}

fun main() {
    val heap = Heap()
    
    heap.print()
    println(heap.push(5, 3))
    heap.print()
    println(heap.push(3, 13))
    heap.print()
}
