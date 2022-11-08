# [level 2] 거리두기 확인하기 - 81302 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/81302) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 2021 카카오 채용연계형 인턴십

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.<br style="user-select: auto;"><br style="user-select: auto;">
코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼<br style="user-select: auto;">
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.</p>

<blockquote style="user-select: auto;">
<ol style="user-select: auto;">
<li style="user-select: auto;">대기실은 5개이며, 각 대기실은 5x5 크기입니다.</li>
<li style="user-select: auto;">거리두기를 위하여 응시자들 끼리는 맨해튼 거리<sup id="fnref1" style="user-select: auto;"><a href="#fn1" style="user-select: auto;">1</a></sup>가 2 이하로 앉지 말아 주세요.</li>
<li style="user-select: auto;">단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.</li>
</ol>
</blockquote>

<p style="user-select: auto;">예를 들어, </p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8c056cac-ec8f-435c-a49a-8125df055c5e/PXP.png" title="" alt="PXP.png" style="user-select: auto;"></th>
<th style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d611f66e-f9c4-4433-91ce-02887657fe7f/PX_XP.png" title="" alt="PX_XP.png" style="user-select: auto;"></th>
<th style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ed707158-0511-457b-9e1a-7dbf34a776a5/PX_OP.png" title="" alt="PX_OP.png" style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="text-align: center; user-select: auto;">위 그림처럼 자리 사이에 파티션이 존재한다면 맨해튼 거리가 2여도 거리두기를 <strong style="user-select: auto;">지킨 것입니다.</strong></td>
<td style="text-align: center; user-select: auto;">위 그림처럼 파티션을 사이에 두고 앉은 경우도 거리두기를 <strong style="user-select: auto;">지킨 것입니다.</strong></td>
<td style="text-align: center; user-select: auto;">위 그림처럼 자리 사이가 맨해튼 거리 2이고 사이에 빈 테이블이 있는 경우는 거리두기를 <strong style="user-select: auto;">지키지 않은 것입니다.</strong></td>
</tr>
<tr style="user-select: auto;">
<td style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/4c548421-1c32-4947-af9e-a45c61501bc4/P.png" title="" alt="P.png" style="user-select: auto;"></td>
<td style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ce799a38-668a-4038-b32f-c515b8701262/O.png" title="" alt="O.png" style="user-select: auto;"></td>
<td style="text-align: center; user-select: auto;"><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/91e8f98b-baeb-4f81-8cb6-5bafebebdcc7/X.png" title="" alt="X.png" style="user-select: auto;"></td>
</tr>
<tr style="user-select: auto;">
<td style="text-align: center; user-select: auto;">응시자가 앉아있는 자리(<code style="user-select: auto;">P</code>)를 의미합니다.</td>
<td style="text-align: center; user-select: auto;">빈 테이블(<code style="user-select: auto;">O</code>)을 의미합니다.</td>
<td style="text-align: center; user-select: auto;">파티션(<code style="user-select: auto;">X</code>)을 의미합니다.</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto;">5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 <code style="user-select: auto;">places</code>가 매개변수로 주어집니다. 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">places</code>의 행 길이(대기실 개수) = 5

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">places</code>의 각 행은 하나의 대기실 구조를 나타냅니다.</li>
</ul></li>
<li style="user-select: auto;"><code style="user-select: auto;">places</code>의 열 길이(대기실 세로 길이) = 5</li>
<li style="user-select: auto;"><code style="user-select: auto;">places</code>의 원소는 <code style="user-select: auto;">P</code>,<code style="user-select: auto;">O</code>,<code style="user-select: auto;">X</code>로 이루어진 문자열입니다.

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">places</code> 원소의 길이(대기실 가로 길이) = 5</li>
<li style="user-select: auto;"><code style="user-select: auto;">P</code>는 응시자가 앉아있는 자리를 의미합니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">O</code>는 빈 테이블을 의미합니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">X</code>는 파티션을 의미합니다.</li>
</ul></li>
<li style="user-select: auto;">입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.</li>
<li style="user-select: auto;">return 값 형식

<ul style="user-select: auto;">
<li style="user-select: auto;">1차원 정수 배열에 5개의 원소를 담아서 return 합니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">places</code>에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.</li>
<li style="user-select: auto;">각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.</li>
</ul></li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">places</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;"><code style="user-select: auto;">[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]</code></td>
<td style="user-select: auto;">[1, 0, 1, 1, 1]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;"><strong style="user-select: auto;">입출력 예 #1</strong></p>

<p style="user-select: auto;">첫 번째 대기실</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">No.</td>
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto;">
<li style="user-select: auto;">모든 응시자가 거리두기를 지키고 있습니다.</li>
</ul>

<p style="user-select: auto;">두 번째 대기실</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">No.</td>
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">0</td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
<td style="user-select: auto;"><strong style="user-select: auto;">P</strong></td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto;">
<li style="user-select: auto;">(0, 0) 자리의 응시자와 (2, 0) 자리의 응시자가 거리두기를 지키고 있지 않습니다.</li>
<li style="user-select: auto;">(1, 2) 자리의 응시자와 (0, 3) 자리의 응시자가 거리두기를 지키고 있지 않습니다.</li>
<li style="user-select: auto;">(4, 3) 자리의 응시자와 (4, 4) 자리의 응시자가 거리두기를 지키고 있지 않습니다.</li>
</ul>

<p style="user-select: auto;">세 번째 대기실</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">No.</td>
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto;">
<li style="user-select: auto;">모든 응시자가 거리두기를 지키고 있습니다.</li>
</ul>

<p style="user-select: auto;">네 번째 대기실</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">No.</td>
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
<td style="user-select: auto;">O</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto;">
<li style="user-select: auto;">대기실에 응시자가 없으므로 거리두기를 지키고 있습니다.</li>
</ul>

<p style="user-select: auto;">다섯 번째 대기실</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
<th style="user-select: auto;"></th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">No.</td>
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">0</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
<td style="user-select: auto;">X</td>
<td style="user-select: auto;">P</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto;">
<li style="user-select: auto;">모든 응시자가 거리두기를 지키고 있습니다.</li>
</ul>

<p style="user-select: auto;">두 번째 대기실을 제외한 모든 대기실에서 거리두기가 지켜지고 있으므로, 배열 [1, 0, 1, 1, 1]을 return 합니다.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한시간 안내</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">정확성 테스트 : 10초</li>
</ul>

<p style="user-select: auto;">※ 공지 - 2022년 4월 25일 테스트케이스가 추가되었습니다.</p>

<div class="footnotes" style="user-select: auto;">
<hr style="user-select: auto;">
<ol style="user-select: auto;">

<li id="fn1" style="user-select: auto;">
<p style="user-select: auto;">두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.&nbsp;<a href="#fnref1" style="user-select: auto;">↩</a></p>
</li>

</ol>
</div>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges