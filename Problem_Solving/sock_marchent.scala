#https://www.hackerrank.com/challenges/sock-merchant

import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {

    // Complete the sockMerchant function below.
    def sockMerchant(n: Int, ar: Array[Int]): Int = {
     val line_group=ar.groupBy(identity)
     val sock_pairs=line_group.map(gr=>gr._2.length/2)
    val sock_sum=sock_pairs.sum
     return sock_sum
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val n = stdin.readLine.trim.toInt

        val ar = stdin.readLine.split(" ").map(_.trim.toInt)
        val result = sockMerchant(n, ar)

        printWriter.println(result)

        printWriter.close()
    }
}
