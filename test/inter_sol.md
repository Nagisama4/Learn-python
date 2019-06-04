### >1. Linux下查找文件

>1. `find`: `find <目录> <条件> <动作>`. Exp: `find / -name 'interfaces'`
>2. `locate`: 查询包含所有本地文件信息的数据库`/var/lib/locatedb`  Exp: `locate interfaces`
>3. `whereis`: 搜索所有二进制文件 Exp: `whereis grep`
>4. `which`: 查看系统命令是否存在，并返回位置 Exp: `which python3`
>5. `type`: 查看命令是否为系统自带命令 Exp: `type cd`

### >2. 复原IP地址

**一种思路是用深度优先算法(DFS)递归来解，避免几种特殊情况，设定边界条件**
>* 生成重复IP
>* IP中存在01.011这样不合适的
>* IP超出4段

```python
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 深度优先遍历
        def dfs(results,result,s,level):
            # print(results,s)
            if len(s) == 0 and level == 4:
                results.add(".".join(result))
                return None
            if level >= 4: # 超出4段ip的话就跳过
                return None
            for i in range(1,4):# 每个ip地址最多三位数字
                if s[:i] != "" and 0 <= int(s[:i]) <= 255: # 保证每段ip不为空 且在0-255
                    if len(s[:i]) >= 2 and s[0] == "0":continue # 保证每段ip没有 01.011.010这样的
                    dfs(results ,result + [s[:i]],s[i:],level + 1)
        results = set()
        dfs(results, [] , s , 0)
        return list(results)

```

### >3. 用队列实现栈

>* 队列（queue）是一种先入先出的数据结构（FIFO）![队列](https://raw.githubusercontent.com/Nagisama4/Learn-python/master/test/queue.png)
>* 栈（stack）是一种后入先出的数据结构（LIFO）![栈](https://raw.githubusercontent.com/Nagisama4/Learn-python/master/test/stack.png)

>1. `push`: 两种数据结构方法相同，都是在数据后面压入新数据
>2. `pop`: 队列的`pop`是从队列的front部分；栈的`pop`是从栈顶，即top部分开始
>3. `top`: 操作位置与`pop`类似，只是只返回值，不删除数据
>4. `empty`: 为真的条件是两个队列都为空

**一种思路是通过两个队列相互配合以实现栈，比如，若A队列存有数据，将数据除了最后一项全部推入B队列，由于是先入先出，数据的顺序不变，A队列还剩下一个数据，当队列的数据仅剩一个时，该数据既是队列的第一个数据，也是队列的最后一个数据，通过`pop()`和`front()`函数的调用，可以产生相应的栈的`pop()`和`top()`的作用**

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queuein = []
        self.queueout = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queuein.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.queuein:
            a = self.queuein.pop(0)
            if self.queuein:
                self.queueout.append(a)
            else:
                return a
        while self.queueout:
            a = self.queueout.pop(0)
            if self.queueout:
                self.queuein.append(a)
            else:
                return a

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.queuein:
            a = self.queuein.pop(0)
            self.queueout.append(a)
            if not self.queuein:
                return a
        while self.queueout:
            a = self.queueout.pop(0)
            self.queuein.append(a)
            if not self.queueout:
                return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queuein and not self.queueout:
            return True
        else:
            return False

```

### >4. 最大子序和

**因为限定了时间复杂度不能为*`O($n^2$)`*，也即是通过暴力循环遍历两遍列表的方法不能用，可以通过动态规划(Dynamic Programming)来解决问题，为简化问题，列表不是全负数组成**
>* 需要一个`head`来保存最优解序列的最大和，`head`会不断变化，再定义一个最优解数组`dp[i]`记录截止到当前元素的最大子序和
>* `list = [-2,1,-3,4,-1,2,1,-5,4]`
>* 最优连续子序列为[4,-1,2,1] ，其和为6
>* 初始化: $dp[0] = -2$
>* -2: $dp[0] = -2$, $head = 0$
>*  1: $dp[1] =  1$, $head = 1$

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)

```
