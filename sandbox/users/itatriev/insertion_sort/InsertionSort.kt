fun insertionSort(arr: IntArray ) {
    for (i in 1..arr.lastIndex) {
        var j = i - 1
        while (j >= 0 && arr[j] > arr[j+1]) {
            arr[j] = arr[j+1].also { arr[j+1] = arr[j] }
            j--
        }
    }
}

fun main() {
    val arr = IntArray(10) { it }.also { it.shuffle() }
    // insertionSort(arr)
    println(arr.contentToString())
}