class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            one_step = i
            two_steps = i

            while True:
                # move one step
                next_one = next_index(one_step)
                if nums[next_one] == 0 or (nums[next_one] > 0) != direction:
                    break
                one_step = next_one

                # move two steps
                next_two = next_index(two_steps)
                if nums[next_two] == 0 or (nums[next_two] > 0) != direction:
                    break
                two_steps = next_two

                next_two = next_index(two_steps)
                if nums[next_two] == 0 or (nums[next_two] > 0) != direction:
                    break
                two_steps = next_two

                if one_step == two_steps:
                    # loop length must be > 1
                    if one_step == next_index(one_step):
                        break
                    return True

            # mark visited path to avoid reprocessing
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                next_j = next_index(j)
                nums[j] = 0
                j = next_j

        return False
