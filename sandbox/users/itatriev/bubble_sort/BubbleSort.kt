import kotlin.random.Random

fun bubbleSort(arr: IntArray) {
    for (i in 1..arr.lastIndex) {
        for (j in 0..arr.lastIndex-i) {
            if (arr[j] > arr[j+1]) {
                arr[j+1] = arr[j].also { arr[j] = arr[j+1] }
            }
        }
    }
}

fun main() {
    val arr = IntArray(10) { it }.also { it.shuffle() }
    bubbleSort(arr)
    println(arr.contentToString())
}