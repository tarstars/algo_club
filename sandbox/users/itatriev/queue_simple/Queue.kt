class Queue(private val size: Int) {
    
    private val arr: IntArray = IntArray(size)
    
    private var l = 0
    private var r = 0
    
    fun push(num: Int): Boolean {
        if (arr[r] != 0) return false // место закончилось
        
        arr[r] = num
		r = (r + 1).mod(size)
        
        return true
    }
    
    fun pop(): Int {
        if (arr[l] == 0) return -1 // пустая очередь
        
        val num = arr[l]
        arr[l] = 0
        l = (l + 1).mod(size)
       
        return num
    }
    
    fun len(): Int = if (r > l) r - l else size - (l - r)
}

fun main() {
   // API
   val q = Queue(5)
   
   q.push(2)
   q.pop()
   
   println(q.len())
}
