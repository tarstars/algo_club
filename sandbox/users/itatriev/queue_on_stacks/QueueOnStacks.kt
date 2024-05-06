class QueueOnStacks(private val size: Int) {
    
    private val pushArr = IntArray(size)
    private val popArr = IntArray(size)
    
    // указывают на ближайшую свободную ячейку
    private var pushHead = 0
    private var popHead = 0
    
    fun push(num: Int): Boolean {
        if (pushHead > pushArr.lastIndex) return false // место закончилось
        
        pushArr[pushHead++] = num
        return true
    }
    
    fun pop(): Int {
        // если 2й стэк пустой
        if (popHead == 0) {
            //println("popHead: $popHead")
            // копируем все из 1го
            while (pushHead > 0) popArr[popHead++] = pushArr[--pushHead]
        }
        
        return if (popHead - 1 < 0) -1 else popArr[--popHead]
    }
}

fun main() {
    val q = QueueOnStacks(5)
    
    println(q.push(4))
    println(q.pop())
}
