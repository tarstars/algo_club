import java.util.ArrayDeque

// https://informatics.msk.ru/mod/statements/view.php?id=255#1

fun main() {
    val n = readLine()?.toIntOrNull() ?: return

    val graphMatrix = Array(n) { IntArray(n) }

    for (p in 0 until n) {
        graphMatrix[p] = readLine()?.split(' ')?.map() {it.toIntOrNull() ?:0}?.toIntArray()?: IntArray(n) {0}
    }

    var (sourceN, destN) = readLine()?.split(' ')?.map() {it.toIntOrNull() ?:0} ?: listOf(0, 0)

    sourceN -= 1
    destN -= 1

    if (sourceN == destN) {
        println(0)
        return
    }

    val graphAdj = hashMapOf<Int, MutableList<Int>>()
    for (p in graphMatrix.indices) {
        graphAdj[p] = mutableListOf()
        for (q in graphMatrix[p].indices) {
            if (graphMatrix[p][q] != 0) {
                graphAdj[p]?.add(q)
            }
        }
    }

    val visited = hashSetOf<Int>()
    val bt = hashMapOf<Int, Int> ()
    val d = hashMapOf<Int, Int> ()
    val que = ArrayDeque<Int> ()

    que.add(sourceN)
    visited.add(sourceN)
    d[sourceN] = 0

    while (que.isNotEmpty()) {
        val current = que.poll()
        for (nei in graphAdj[current]?:listOf()) {
            if (!visited.contains(nei)) {
                visited.add(nei)
                que.add(nei)
                bt[nei] = current
                d[nei] = (d[current]?:0) + 1
            }
        }
    }

    if (!visited.contains(destN)) {
        println(-1)
        return
    }

    val path:MutableList<Int> = mutableListOf()
    var pos = destN

    while (pos != sourceN) {
        path.add(pos)
        pos = bt[pos]?:0
    }
    path.add(pos)

    path.reverse()

    println(path.size - 1)
    println((path.map {it + 1}).joinToString(" "))
}
