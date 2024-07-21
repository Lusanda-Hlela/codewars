using System;
public class Kata
{
  public static double DistanceBetweenPoints(Point a, Point b)
  {
    double dX = Math.Abs(a.X - b.X);
    double dY = Math.Abs(a.Y - b.Y);
    double pSum = Math.Pow(dX, 2) + Math.Pow(dY, 2);
    double result = Math.Sqrt(pSum);
    return result;
  }
}