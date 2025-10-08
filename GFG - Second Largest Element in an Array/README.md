# Second Largest 

  <h2 style="margin-top: 0; border-bottom: 1px solid #eee; padding-bottom: 5px;">Problem Detayları</h2>

  <p>
    Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
  </p>
  
  <p style="font-weight: bold; color: #ffffffff;">
    Not: İkinci en büyük eleman, en büyük elemana eşit olmamalıdır.
  </p>

  <h3 style="margin-top: 15px;">Examples</h3>

  <div style="background-color: #fff; padding: 10px; border: 1px solid #eee; border-radius: 4px; margin-bottom: 10px; color:#000000;">
    <strong>Input:</strong> <code>arr[] = [12, 35, 1, 10, 34, 1]</code><br>
    <strong>Output:</strong> <code>34</code><br>
    <strong>Explanation:</strong> Dizinin en büyük elemanı 35 ve ikinci en büyük elemanı 34'tür.
  </div>
  
  <div style="background-color: #fff; padding: 10px; border: 1px solid #eee; border-radius: 4px; margin-bottom: 10px; color:#000000;">
    <strong>Input:</strong> <code>arr[] = [10, 5, 10]</code><br>
    <strong>Output:</strong> <code>5</code><br>
    <strong>Explanation:</strong> Dizinin en büyük elemanı 10 ve ikinci en büyük elemanı 5'tir.
  </div>
  
  <div style="background-color: #fff; padding: 10px; border: 1px solid #eee; border-radius: 4px; color:#000000;">
    <strong>Input:</strong> <code>arr[] = [10, 10, 10]</code><br>
    <strong>Output:</strong> <code>-1</code><br>
    <strong>Explanation:</strong> Dizinin en büyük elemanı 10 ve ikinci en büyük eleman mevcut değildir (çünkü en büyük elemanla aynı olmamalıdır).
  </div>

  <h3 style="margin-top: 15px;">Constraints</h3>
  <ul style="list-style-type: none; padding-left: 0;">
    <li style="margin-bottom: 5px;">• <code>2 ≤ arr.size() ≤ 10<sup>5</sup></code></li>
    <li>• <code>1 ≤ arr[i] ≤ 10<sup>5</sup></code></li>
  </ul>
</div>