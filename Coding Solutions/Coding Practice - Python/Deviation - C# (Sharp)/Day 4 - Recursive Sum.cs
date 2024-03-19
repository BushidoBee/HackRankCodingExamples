{
    var sum = 0L;
    n.ToList().ForEach(c => sum += Convert.ToInt64(Char.GetNumericValue(c)));
    if (k > 1) sum += sum * (k - 1);
    return superDigit(Convert.ToString(sum), 1);
}
