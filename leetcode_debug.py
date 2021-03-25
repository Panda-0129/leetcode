import random


def largestRectangleArea(heights) -> int:
    stack = []
    res = 0
    # stack中记录下标
    for i in range(len(heights)):
        # 当前高度小于左边柱形高度时，可以确定以左边柱形为高度的最大矩形面积
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            # 左边柱形高度等于当前高度时
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            # 确定当前矩形宽度
            if len(stack) > 0:
                cur_width = i - stack[-1] - 1
            else:
                cur_width = i

            res = max(cur_width * cur_height, res)
        stack.append(i)

    while len(stack) > 0:
        cur_height = heights[stack.pop()]
        while len(stack) > 0 and cur_height == heights[stack[-1]]:
            stack.pop()

        if len(stack) > 0:
            cur_width = len(heights) - stack[-1] - 1
        else:
            cur_width = len(heights)

        res = max(cur_width * cur_height, res)

    return res


if __name__ == '__main__':
    print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
