from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game
from django.shortcuts import get_object_or_404

    #chess notation into unicode figures
UNICODE_PIECES = {
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟︎',
}

def new_game(request):
    if request.method == 'POST':
        form = GameForm(data=request.POST)
        if form.is_valid():
            white = form.cleaned_data.get('player_white') or 'white'
            black = form.cleaned_data.get('player_black') or 'black'
            game = Game.objects.create(
                player_white=white,
                player_black=black,
                board_state='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
            )
            return redirect('game_detail', game_id=game.id)

    else:
        form = GameForm()
    
    return render(request, 'game/new_game.html', {'form': form})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    #FEN into 2D
    board_fen = game.board_state.split()[0]
    rows = board_fen.split('/')

    board = []
    for row_index, row in enumerate(rows):
        expanded_row = []
        for char in row:
            if char.isdigit():
                expanded_row.extend(['']*int(char))
            else:
                symbol = UNICODE_PIECES.get(char, char)
                expanded_row.append(symbol)

        #coordinations for js template
        row_data = {
            'row_num': 8 - row_index,
            'squares': [
                {'col_letter': chr(ord('a') + col_index), 'value': square}
                for col_index, square in enumerate(expanded_row)
            ]
        }
        board.append(row_data)
        

    return render(request, 'game/game_detail.html', {'game': game, 'board':board})


