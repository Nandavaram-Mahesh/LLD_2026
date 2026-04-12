class TicTacToe:
    # Step 1: Board Initialization
    def __init__(self,board_rows,board_cells):
        # Board State
        self.board = [["" for _ in range(board_cells)] for _ in range(board_rows)]
        
        # Player State
        self.current_player = "X"
        
        # Game state
        self.game_over = False
    
    # Step 2: Display
    def display_board(self):
        print("\n 0   1   2")
        
        for r in range(3):
            row_display=f'{r}'
            for c in range(3):
                cell = self.board[r][c] if self.board[r][c] else '.'
                row_display+=f' {cell} '
                if c<2:
                    row_display += "|"
            print(row_display)
            if r<2:
                print("  ---+---+---")
        print()
        
    # Step 3: Make Move (with Validation)
    def make_move(self,r,c):
        # ── PATTERN: always validate BEFORE applying the move ──────
        rows,cols = len(self.board),len(self.board[0])
        
        # Check 1: Is the game still going?
        if self.game_over:
            print("Game is over!")
            return False
        
        # Check 2: Is (row, col) inside the board?
        if not 0<=r<rows and 0<=c<cols:
            print("Out of bounds!")
            return False
        
        # Check 3: Is the cell empty?
        if self.board[r][c]!='':
            print("Cell already taken!")
            return False
        
        # All checks passed → place the mark
        self.board[r][c]= self.current_player
        return True
    
    # Step 4: Win Detection (The Core Logic)
    def check_winner(self):
        # ── PATTERN: check all winning lines one by one ───────────
        b = self.board  
        # Check all 3 rows
        for r in range(3):
            if b[r][0]==b[r][1]==b[r][2]!='':
                return b[r][0]
        # Check all 3 columns
        for c in range(3):
            if b[0][c]==b[1][c]==b[2][c]!='':
                return b[0][c] 
        # Check main diagonal (top-left → bottom-right)
        if b[0][0]==b[1][1]==b[2][2]!='':
            return b[1][1]
        # Check anti-diagonal (top-right → bottom-left)
        if b[0][2]==b[1][1]==b[0][0]!='':
            return b[1][1]
        # Check for draw (no empty cells left)
        for r in range(3):
            for c in range(3):
                if b[r][c]=='':
                    return None
        return "Draw"
    
    def switch_player(self):
        self.current_player = "O" if self.current_player=="X" else "X"

    # Step 5: The Game Loop (Ties It All Together)
    def play(self):
    # ── PATTERN: the universal game loop ───────────────────────   
        print("=== TIC TAC TOE ===")
        
        while not self.game_over:
            # 1. Show current board
            self.display_board()
            # 2. Get player input
            print(f"Player {self.current_player}'s turn")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Please enter numbers only!")
                continue
            # 3. Try to make the move
            if not self.make_move(row,col):
                continue   # invalid move, ask again
            # 4. Check if game is over
            result = self.check_winner()
            if result:
                self.display_board()
                if result =="Draw":
                    print("It's a draw!")
                else:
                    print(f"🏆 Player {result} wins!")
                self.game_over = True
                break
            # 5. Switch to next player
            self.switch_player()
# Client Code
game = TicTacToe(3,3)
game.play()

