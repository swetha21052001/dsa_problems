class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rq = []
        cq = []
        rq.append(sr)
        cq.append(sc)
        #create vectors for directions
        rv = [-1,+1,0,0]
        cv = [0,0,+1,-1]
        #copy the current color
        curr = image[sr][sc]
        while rq:
            r = rq.pop(0)
            c = cq.pop(0)
            image[r][c] = color
            for i in range(0,4):
                ind = r+rv[i]
                jnd = c+cv[i]
                #check for edges of matrix
                if ind<0 or jnd<0 or ind>=len(image) or jnd >= len(image[0]):
                    continue
                #if the cell is already colored skip
                if image[ind][jnd] == color:
                    continue
                #if the cell color is different from the original source node skip
                if image[ind][jnd] != curr:
                    continue
                rq.append(ind)
                cq.append(jnd)
        return image




        
