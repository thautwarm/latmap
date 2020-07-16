
"""
Copyright thautwarm (c) 2019

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

    * Neither the name of thautwarm nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from theme import Theme
Keyword = Theme.Keyword
Var = Theme.Var
Literal = Theme.Literal
Pattern = Theme.Pattern
String = Theme.String
Call = Theme.Call
Type = Theme.Type

def append(x, a):
    x.append(a)
    return x

from typing import Generic, TypeVar
T = TypeVar('T')

class Tokens():
    __slots__ = ['array', 'offset']

    def __init__(self, array):
        self.array = array
        self.offset = 0

class State():

    def __init__(self):
        pass

class AST(Generic[T]):
    __slots__ = ['tag', 'contents']

    def __init__(self, tag: str, contents: T):
        self.tag = tag
        self.contents = contents

class Nil():
    nil = None
    __slots__ = []

    def __init__(self):
        if (Nil.nil is None):
            Nil.nil = self
            return
        raise ValueError('Nil cannot get instantiated twice.')

    def __len__(self):
        return 0

    def __getitem__(self, n):
        raise IndexError('Out of bounds')

    @property
    def head(self):
        raise IndexError('Out of bounds')

    @property
    def tail(self):
        raise IndexError('Out of bounds')

    def __repr__(self):
        return '[]'
_nil = Nil()

class Cons():
    __slots__ = ['head', 'tail']

    def __init__(self, _head, _tail):
        self.head = _head
        self.tail = _tail

    def __len__(self):
        nil = _nil
        l = 0
        while (self is not nil):
            l += 1
            self = self.tail
        return l

    def __iter__(self):
        nil = _nil
        while (self is not nil):
            (yield self.head)
            self = self.tail

    def __getitem__(self, n):
        while (n != 0):
            self = self.tail
            n -= 1
        return self.head

    def __repr__(self):
        return repr(list(self))
try:

    def mk_pretty():
        from prettyprinter import register_pretty, pretty_call, pprint

        @register_pretty(Tokens)
        def pretty_tokens(value, ctx):
            return pretty_call(ctx, Tokens, offset=value.offset, array=value.array)

        @register_pretty(AST)
        def pretty_ast(value, ctx):
            return pretty_call(ctx, AST, tag=value.tag, contents=value.contents)
    mk_pretty()
    del mk_pretty
except ImportError:
    pass
del T, Generic, TypeVar
builtin_cons = Cons
builtin_nil = _nil
builtin_mk_ast = AST

def mk_parser(s, ss, partial_ok):
    pass

    def rbnf_named_lr_step_lang(rbnf_tmp_0, builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 5):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_1 = lcl_0
        lcl_0 = (rbnf_tmp_1 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote ( not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_1 = lcl_1
            try:
                builtin_tokens.array[(builtin_tokens.offset + 0)]
                _rbnf_peek_tmp = True
            except IndexError:
                _rbnf_peek_tmp = False
            lcl_1 = _rbnf_peek_tmp
            if lcl_1:
                lcl_3 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                lcl_3 = lcl_3.idint
                if (lcl_3 == 7):
                    lcl_4 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 6):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote ) not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, Call, rbnf_tmp_3, Call)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 6):
                    _rbnf_old_offset = builtin_tokens.offset
                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_2 = lcl_4
                    lcl_4 = ss(rbnf_tmp_1, Call, rbnf_tmp_2, Call)
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_2 = lcl_4
                elif (lcl_3 == 5):
                    lcl_4 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 6):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote ) not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, Call, rbnf_tmp_3, Call)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 18):
                    lcl_4 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 6):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote ) not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, Call, rbnf_tmp_3, Call)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 17):
                    lcl_4 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 6):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote ) not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, Call, rbnf_tmp_3, Call)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 1):
                    lcl_4 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 6):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote ) not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, Call, rbnf_tmp_3, Call)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                else:
                    lcl_4 = (rbnf_named__off_1, 'lang lookahead failed')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_2 = lcl_4
                lcl_1 = lcl_2
            else:
                lcl_2 = (rbnf_named__off_1, 'lang got EOF')
                lcl_2 = builtin_cons(lcl_2, builtin_nil)
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_lang(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_lang_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_lang(rbnf_named_lr_lang_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_lang_try = lcl_0
        lcl_0 = rbnf_named_lr_lang_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_lang_try[1]
            rbnf_named_lr_lang_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_lang(rbnf_named_lr_lang_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_lang_try = lcl_1
            lcl_1 = rbnf_named_lr_lang_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_lang_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_lang_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_0(rbnf_tmp_0, builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_comma(builtin_state, builtin_tokens)
        rbnf_named__check_1 = lcl_0
        lcl_0 = rbnf_named__check_1[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_1
        else:
            lcl_1 = rbnf_named__check_1[1]
            rbnf_tmp_1 = lcl_1
            lcl_1 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_0(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_0_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_0(rbnf_named_lr_rbnfmacro_0_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_0_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_0_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_0_try[1]
            rbnf_named_lr_rbnfmacro_0_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_0(rbnf_named_lr_rbnfmacro_0_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_0_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_0_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_0_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_0_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_1(rbnf_tmp_0, builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_atomExpr(builtin_state, builtin_tokens)
        rbnf_named__check_1 = lcl_0
        lcl_0 = rbnf_named__check_1[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_1
        else:
            lcl_1 = rbnf_named__check_1[1]
            rbnf_tmp_1 = lcl_1
            lcl_1 = append(rbnf_tmp_0, rbnf_tmp_1)
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_1(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_1_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_1(rbnf_named_lr_rbnfmacro_1_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_1_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_1_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_1_try[1]
            rbnf_named_lr_rbnfmacro_1_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_1(rbnf_named_lr_rbnfmacro_1_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_1_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_1_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_1_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_1_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_2(rbnf_tmp_0, builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_xor(builtin_state, builtin_tokens)
        rbnf_named__check_1 = lcl_0
        lcl_0 = rbnf_named__check_1[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_1
        else:
            lcl_1 = rbnf_named__check_1[1]
            rbnf_tmp_1 = lcl_1
            lcl_1 = rbnf_named_parse_cseq(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_2(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_2_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_2(rbnf_named_lr_rbnfmacro_2_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_2_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_2_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_2_try[1]
            rbnf_named_lr_rbnfmacro_2_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_2(rbnf_named_lr_rbnfmacro_2_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_2_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_2_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_2_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_2_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_3(rbnf_tmp_0, builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_xor(builtin_state, builtin_tokens)
        rbnf_named__check_1 = lcl_0
        lcl_0 = rbnf_named__check_1[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_1
        else:
            lcl_1 = rbnf_named__check_1[1]
            rbnf_tmp_1 = lcl_1
            lcl_1 = rbnf_named_parse_rewrite(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_3(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_3_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_3(rbnf_named_lr_rbnfmacro_3_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_3_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_3_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_3_try[1]
            rbnf_named_lr_rbnfmacro_3_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_3(rbnf_named_lr_rbnfmacro_3_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_3_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_3_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_3_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_3_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_4(rbnf_tmp_0, builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_comma(builtin_state, builtin_tokens)
        rbnf_named__check_1 = lcl_0
        lcl_0 = rbnf_named__check_1[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_1
        else:
            lcl_1 = rbnf_named__check_1[1]
            rbnf_tmp_1 = lcl_1
            lcl_1 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_4(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_4_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_4(rbnf_named_lr_rbnfmacro_4_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_4_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_4_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_4_try[1]
            rbnf_named_lr_rbnfmacro_4_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_4(rbnf_named_lr_rbnfmacro_4_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_4_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_4_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_4_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_4_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_5(rbnf_tmp_0, builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 0):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_1 = lcl_0
        lcl_0 = (rbnf_tmp_1 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote , not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = rbnf_named_parse_lang(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_5(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_5_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_5(rbnf_named_lr_rbnfmacro_5_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_5_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_5_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_5_try[1]
            rbnf_named_lr_rbnfmacro_5_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_5(rbnf_named_lr_rbnfmacro_5_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_5_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_5_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_5_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_5_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_6(rbnf_tmp_0, builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 0):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_1 = lcl_0
        lcl_0 = (rbnf_tmp_1 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote , not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = rbnf_named_parse_filename(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_6(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_6_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_6(rbnf_named_lr_rbnfmacro_6_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_6_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_6_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_6_try[1]
            rbnf_named_lr_rbnfmacro_6_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_6(rbnf_named_lr_rbnfmacro_6_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_6_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_6_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_6_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_6_try
        return lcl_0

    def rbnf_named_lr_step_rbnfmacro_7(rbnf_tmp_0, builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 0):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_1 = lcl_0
        lcl_0 = (rbnf_tmp_1 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote , not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
            rbnf_named__check_2 = lcl_1
            lcl_1 = rbnf_named__check_2[0]
            lcl_1 = (lcl_1 == False)
            if lcl_1:
                lcl_1 = rbnf_named__check_2
            else:
                lcl_2 = rbnf_named__check_2[1]
                rbnf_tmp_2 = lcl_2
                lcl_2 = append(rbnf_tmp_0, rbnf_tmp_2)
                rbnf_tmp_1_ = lcl_2
                lcl_2 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_lr_loop_rbnfmacro_7(rbnf_tmp_0, builtin_state, builtin_tokens):
        rbnf_named_lr_rbnfmacro_7_reduce = rbnf_tmp_0
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        lcl_0 = rbnf_named_lr_step_rbnfmacro_7(rbnf_named_lr_rbnfmacro_7_reduce, builtin_state, builtin_tokens)
        rbnf_named_lr_rbnfmacro_7_try = lcl_0
        lcl_0 = rbnf_named_lr_rbnfmacro_7_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_7_try[1]
            rbnf_named_lr_rbnfmacro_7_reduce = lcl_1
            lcl_1 = rbnf_named_lr_step_rbnfmacro_7(rbnf_named_lr_rbnfmacro_7_reduce, builtin_state, builtin_tokens)
            rbnf_named_lr_rbnfmacro_7_try = lcl_1
            lcl_1 = rbnf_named_lr_rbnfmacro_7_try[0]
            lcl_1 = (lcl_1 is not False)
            lcl_0 = lcl_1
        lcl_0 = builtin_tokens.offset
        lcl_0 = (lcl_0 == rbnf_named__off_0)
        if lcl_0:
            lcl_1 = (True, rbnf_named_lr_rbnfmacro_7_reduce)
            lcl_0 = lcl_1
        else:
            lcl_0 = rbnf_named_lr_rbnfmacro_7_try
        return lcl_0

    def rbnf_named_parse_Ident(builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 1):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_0 = lcl_0
        lcl_0 = (rbnf_tmp_0 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'Ident not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = s(rbnf_tmp_0, Var)
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_IdentList(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_4(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_START(builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 22):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_0 = lcl_0
        lcl_0 = (rbnf_tmp_0 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'BOF not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_1 = lcl_1
            try:
                builtin_tokens.array[(builtin_tokens.offset + 0)]
                _rbnf_peek_tmp = True
            except IndexError:
                _rbnf_peek_tmp = False
            lcl_1 = _rbnf_peek_tmp
            if lcl_1:
                lcl_3 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                lcl_3 = lcl_3.idint
                if (lcl_3 == 20):
                    lcl_4 = rbnf_named_parse_pragma(builtin_state, builtin_tokens)
                    rbnf_named__check_1 = lcl_4
                    lcl_4 = rbnf_named__check_1[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_1
                    else:
                        lcl_5 = rbnf_named__check_1[1]
                        rbnf_tmp_1 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 23):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_2 = lcl_5
                        lcl_5 = (rbnf_tmp_2 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'EOF not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = partial_ok()
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 19):
                    lcl_4 = rbnf_named_parse_pragma(builtin_state, builtin_tokens)
                    rbnf_named__check_1 = lcl_4
                    lcl_4 = rbnf_named__check_1[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_1
                    else:
                        lcl_5 = rbnf_named__check_1[1]
                        rbnf_tmp_1 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 23):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_2 = lcl_5
                        lcl_5 = (rbnf_tmp_2 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'EOF not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = partial_ok()
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 1):
                    lcl_4 = builtin_tokens.offset
                    rbnf_named__off_2 = lcl_4
                    try:
                        builtin_tokens.array[(builtin_tokens.offset + 1)]
                        _rbnf_peek_tmp = True
                    except IndexError:
                        _rbnf_peek_tmp = False
                    lcl_4 = _rbnf_peek_tmp
                    if lcl_4:
                        lcl_6 = builtin_tokens.array[(builtin_tokens.offset + 1)]
                        lcl_6 = lcl_6.idint
                        if (lcl_6 == 7):
                            lcl_7 = rbnf_named_parse_prod(builtin_state, builtin_tokens)
                            rbnf_named__check_1 = lcl_7
                            lcl_7 = rbnf_named__check_1[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_1
                            else:
                                lcl_8 = rbnf_named__check_1[1]
                                rbnf_tmp_1 = lcl_8
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 23):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_8 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = (rbnf_tmp_2 is None)
                                if lcl_8:
                                    lcl_9 = builtin_tokens.offset
                                    lcl_9 = (lcl_9, 'EOF not match')
                                    lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                    lcl_9 = (False, lcl_9)
                                    lcl_8 = lcl_9
                                else:
                                    lcl_9 = partial_ok()
                                    rbnf_tmp_1_ = lcl_9
                                    lcl_9 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_9
                                lcl_7 = lcl_8
                            lcl_5 = lcl_7
                        elif (lcl_6 == 16):
                            lcl_7 = rbnf_named_parse_prod(builtin_state, builtin_tokens)
                            rbnf_named__check_1 = lcl_7
                            lcl_7 = rbnf_named__check_1[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_1
                            else:
                                lcl_8 = rbnf_named__check_1[1]
                                rbnf_tmp_1 = lcl_8
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 23):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_8 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = (rbnf_tmp_2 is None)
                                if lcl_8:
                                    lcl_9 = builtin_tokens.offset
                                    lcl_9 = (lcl_9, 'EOF not match')
                                    lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                    lcl_9 = (False, lcl_9)
                                    lcl_8 = lcl_9
                                else:
                                    lcl_9 = partial_ok()
                                    rbnf_tmp_1_ = lcl_9
                                    lcl_9 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_9
                                lcl_7 = lcl_8
                            lcl_5 = lcl_7
                        elif (lcl_6 == 14):
                            lcl_7 = rbnf_named_parse_prod(builtin_state, builtin_tokens)
                            rbnf_named__check_1 = lcl_7
                            lcl_7 = rbnf_named__check_1[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_1
                            else:
                                lcl_8 = rbnf_named__check_1[1]
                                rbnf_tmp_1 = lcl_8
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 23):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_8 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = (rbnf_tmp_2 is None)
                                if lcl_8:
                                    lcl_9 = builtin_tokens.offset
                                    lcl_9 = (lcl_9, 'EOF not match')
                                    lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                    lcl_9 = (False, lcl_9)
                                    lcl_8 = lcl_9
                                else:
                                    lcl_9 = partial_ok()
                                    rbnf_tmp_1_ = lcl_9
                                    lcl_9 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_9
                                lcl_7 = lcl_8
                            lcl_5 = lcl_7
                        elif (lcl_6 == 21):
                            lcl_7 = rbnf_named_parse_pragma(builtin_state, builtin_tokens)
                            rbnf_named__check_1 = lcl_7
                            lcl_7 = rbnf_named__check_1[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_1
                            else:
                                lcl_8 = rbnf_named__check_1[1]
                                rbnf_tmp_1 = lcl_8
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 23):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_8 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = (rbnf_tmp_2 is None)
                                if lcl_8:
                                    lcl_9 = builtin_tokens.offset
                                    lcl_9 = (lcl_9, 'EOF not match')
                                    lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                    lcl_9 = (False, lcl_9)
                                    lcl_8 = lcl_9
                                else:
                                    lcl_9 = partial_ok()
                                    rbnf_tmp_1_ = lcl_9
                                    lcl_9 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_9
                                lcl_7 = lcl_8
                            lcl_5 = lcl_7
                        else:
                            lcl_7 = rbnf_named_parse_prod(builtin_state, builtin_tokens)
                            rbnf_named__check_1 = lcl_7
                            lcl_7 = rbnf_named__check_1[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_1
                            else:
                                lcl_8 = rbnf_named__check_1[1]
                                rbnf_tmp_1 = lcl_8
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 23):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_8 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = (rbnf_tmp_2 is None)
                                if lcl_8:
                                    lcl_9 = builtin_tokens.offset
                                    lcl_9 = (lcl_9, 'EOF not match')
                                    lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                    lcl_9 = (False, lcl_9)
                                    lcl_8 = lcl_9
                                else:
                                    lcl_9 = partial_ok()
                                    rbnf_tmp_1_ = lcl_9
                                    lcl_9 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_9
                                lcl_7 = lcl_8
                            lcl_5 = lcl_7
                        lcl_4 = lcl_5
                    else:
                        lcl_5 = (rbnf_named__off_2, 'START got EOF')
                        lcl_5 = builtin_cons(lcl_5, builtin_nil)
                        lcl_5 = (False, lcl_5)
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                elif (lcl_3 == 23):
                    _rbnf_old_offset = builtin_tokens.offset
                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_1 = lcl_4
                    lcl_4 = ()
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_2 = lcl_4
                elif (lcl_3 == 21):
                    lcl_4 = rbnf_named_parse_pragma(builtin_state, builtin_tokens)
                    rbnf_named__check_1 = lcl_4
                    lcl_4 = rbnf_named__check_1[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_1
                    else:
                        lcl_5 = rbnf_named__check_1[1]
                        rbnf_tmp_1 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 23):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_2 = lcl_5
                        lcl_5 = (rbnf_tmp_2 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'EOF not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = partial_ok()
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                else:
                    lcl_4 = (rbnf_named__off_1, 'START lookahead failed')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_2 = lcl_4
                lcl_1 = lcl_2
            else:
                lcl_2 = (rbnf_named__off_1, 'START got EOF')
                lcl_2 = builtin_cons(lcl_2, builtin_nil)
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_alts(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_3(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_atom(builtin_state, builtin_tokens):
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        try:
            builtin_tokens.array[(builtin_tokens.offset + 0)]
            _rbnf_peek_tmp = True
        except IndexError:
            _rbnf_peek_tmp = False
        lcl_0 = _rbnf_peek_tmp
        if lcl_0:
            lcl_2 = builtin_tokens.array[(builtin_tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 3):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                rbnf_named__check_1 = lcl_3
                lcl_3 = rbnf_named__check_1[0]
                lcl_3 = (lcl_3 == False)
                if lcl_3:
                    lcl_3 = rbnf_named__check_1
                else:
                    lcl_4 = rbnf_named__check_1[1]
                    rbnf_tmp_1 = lcl_4
                    try:
                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                        if (_rbnf_cur_token.idint is 4):
                            builtin_tokens.offset += 1
                        else:
                            _rbnf_cur_token = None
                    except IndexError:
                        _rbnf_cur_token = None
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_2 = lcl_4
                    lcl_4 = (rbnf_tmp_2 is None)
                    if lcl_4:
                        lcl_5 = builtin_tokens.offset
                        lcl_5 = (lcl_5, 'quote > not match')
                        lcl_5 = builtin_cons(lcl_5, builtin_nil)
                        lcl_5 = (False, lcl_5)
                        lcl_4 = lcl_5
                    else:
                        lcl_5 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                        rbnf_tmp_1_ = lcl_5
                        lcl_5 = (True, rbnf_tmp_1_)
                        lcl_4 = lcl_5
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 5):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                rbnf_named__check_1 = lcl_3
                lcl_3 = rbnf_named__check_1[0]
                lcl_3 = (lcl_3 == False)
                if lcl_3:
                    lcl_3 = rbnf_named__check_1
                else:
                    lcl_4 = rbnf_named__check_1[1]
                    rbnf_tmp_1 = lcl_4
                    try:
                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                        if (_rbnf_cur_token.idint is 6):
                            builtin_tokens.offset += 1
                        else:
                            _rbnf_cur_token = None
                    except IndexError:
                        _rbnf_cur_token = None
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_2 = lcl_4
                    lcl_4 = (rbnf_tmp_2 is None)
                    if lcl_4:
                        lcl_5 = builtin_tokens.offset
                        lcl_5 = (lcl_5, 'quote ) not match')
                        lcl_5 = builtin_cons(lcl_5, builtin_nil)
                        lcl_5 = (False, lcl_5)
                        lcl_4 = lcl_5
                    else:
                        lcl_5 = ss(rbnf_tmp_0, Keyword, rbnf_tmp_2, Keyword)
                        rbnf_tmp_1_ = lcl_5
                        lcl_5 = (True, rbnf_tmp_1_)
                        lcl_4 = lcl_5
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 2):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = s(rbnf_tmp_0, Literal)
                rbnf_tmp_1_ = lcl_3
                lcl_3 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_3
            elif (lcl_2 == 1):
                lcl_3 = builtin_tokens.offset
                rbnf_named__off_1 = lcl_3
                try:
                    builtin_tokens.array[(builtin_tokens.offset + 1)]
                    _rbnf_peek_tmp = True
                except IndexError:
                    _rbnf_peek_tmp = False
                lcl_3 = _rbnf_peek_tmp
                if lcl_3:
                    lcl_5 = builtin_tokens.array[(builtin_tokens.offset + 1)]
                    lcl_5 = lcl_5.idint
                    if (lcl_5 == 7):
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_0 = lcl_6
                        lcl_6 = builtin_tokens.offset
                        rbnf_named__off_2 = lcl_6
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_6
                        lcl_6 = rbnf_named_parse_expr_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_2 = lcl_6
                        lcl_6 = rbnf_named__check_2[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_2
                        else:
                            lcl_7 = rbnf_named__check_2[1]
                            rbnf_tmp_2 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_3 = lcl_7
                            lcl_7 = (rbnf_tmp_3 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Pattern, rbnf_tmp_1, Keyword, rbnf_tmp_3, Keyword)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 9):
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_0 = lcl_6
                        lcl_6 = builtin_tokens.offset
                        rbnf_named__off_2 = lcl_6
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_6
                        lcl_6 = rbnf_named_parse_atomExpr(builtin_state, builtin_tokens)
                        rbnf_named__check_2 = lcl_6
                        lcl_6 = rbnf_named__check_2[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_2
                        else:
                            lcl_7 = rbnf_named__check_2[1]
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = ss(rbnf_tmp_0, Call, rbnf_tmp_1, Keyword)
                            rbnf_tmp_1_ = lcl_7
                            lcl_7 = (True, rbnf_tmp_1_)
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    else:
                        lcl_6 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                        rbnf_named__check_0 = lcl_6
                        lcl_6 = rbnf_named__check_0[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_0
                        else:
                            lcl_7 = rbnf_named__check_0[1]
                            rbnf_tmp_0 = lcl_7
                            lcl_7 = ()
                            rbnf_tmp_1_ = lcl_7
                            lcl_7 = (True, rbnf_tmp_1_)
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    lcl_3 = lcl_4
                else:
                    lcl_4 = (rbnf_named__off_1, 'atom got EOF')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            else:
                lcl_3 = (rbnf_named__off_0, 'atom lookahead failed')
                lcl_3 = builtin_cons(lcl_3, builtin_nil)
                lcl_3 = (False, lcl_3)
                lcl_1 = lcl_3
            lcl_0 = lcl_1
        else:
            lcl_1 = (rbnf_named__off_0, 'atom got EOF')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_atomExpr(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_atom(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            try:
                builtin_tokens.array[(builtin_tokens.offset + 0)]
                _rbnf_peek_tmp = True
            except IndexError:
                _rbnf_peek_tmp = False
            lcl_1 = _rbnf_peek_tmp
            if lcl_1:
                lcl_3 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                lcl_3 = lcl_3.idint
                if (lcl_3 == 10):
                    _rbnf_old_offset = builtin_tokens.offset
                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_1 = lcl_4
                    lcl_4 = s(rbnf_tmp_1, Call)
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_2 = lcl_4
                else:
                    lcl_4 = ()
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_2 = lcl_4
                lcl_1 = lcl_2
            else:
                lcl_2 = (rbnf_named__off_0, 'atomExpr got EOF')
                lcl_2 = builtin_cons(lcl_2, builtin_nil)
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_comma(builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 0):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_0 = lcl_0
        lcl_0 = (rbnf_tmp_0 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote , not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = s(rbnf_tmp_0, String)
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_cseq(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_seq(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_expr(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_2(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_expr_lst(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_0(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_filename(builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 2):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_0 = lcl_0
        lcl_0 = (rbnf_tmp_0 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'QuotedStr not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = s(rbnf_tmp_0, String)
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_lang(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_lang_atom(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_lang(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_lang_atom(builtin_state, builtin_tokens):
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        try:
            builtin_tokens.array[(builtin_tokens.offset + 0)]
            _rbnf_peek_tmp = True
        except IndexError:
            _rbnf_peek_tmp = False
        lcl_0 = _rbnf_peek_tmp
        if lcl_0:
            lcl_2 = builtin_tokens.array[(builtin_tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 7):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = builtin_tokens.offset
                rbnf_named__off_1 = lcl_3
                try:
                    builtin_tokens.array[(builtin_tokens.offset + 0)]
                    _rbnf_peek_tmp = True
                except IndexError:
                    _rbnf_peek_tmp = False
                lcl_3 = _rbnf_peek_tmp
                if lcl_3:
                    lcl_5 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                    lcl_5 = lcl_5.idint
                    if (lcl_5 == 8):
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_6
                        lcl_6 = ss(rbnf_tmp_0, Type, rbnf_tmp_1, Type)
                        rbnf_tmp_1_ = lcl_6
                        lcl_6 = (True, rbnf_tmp_1_)
                        lcl_4 = lcl_6
                    elif (lcl_5 == 7):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = (rbnf_tmp_2 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 5):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = (rbnf_tmp_2 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 18):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = (rbnf_tmp_2 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 17):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = (rbnf_tmp_2 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 1):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 8):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_7 = _rbnf_cur_token
                            rbnf_tmp_2 = lcl_7
                            lcl_7 = (rbnf_tmp_2 is None)
                            if lcl_7:
                                lcl_8 = builtin_tokens.offset
                                lcl_8 = (lcl_8, 'quote ] not match')
                                lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                lcl_8 = (False, lcl_8)
                                lcl_7 = lcl_8
                            else:
                                lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    else:
                        lcl_6 = (rbnf_named__off_1, 'lang_atom lookahead failed')
                        lcl_6 = builtin_cons(lcl_6, builtin_nil)
                        lcl_6 = (False, lcl_6)
                        lcl_4 = lcl_6
                    lcl_3 = lcl_4
                else:
                    lcl_4 = (rbnf_named__off_1, 'lang_atom got EOF')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 5):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = builtin_tokens.offset
                rbnf_named__off_1 = lcl_3
                try:
                    builtin_tokens.array[(builtin_tokens.offset + 0)]
                    _rbnf_peek_tmp = True
                except IndexError:
                    _rbnf_peek_tmp = False
                lcl_3 = _rbnf_peek_tmp
                if lcl_3:
                    lcl_5 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                    lcl_5 = lcl_5.idint
                    if (lcl_5 == 7):
                        lcl_6 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            lcl_7 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_7
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_7 = _rbnf_peek_tmp
                            if lcl_7:
                                lcl_9 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_9 = lcl_9.idint
                                if (lcl_9 == 0):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_10 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_10
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 6):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_10 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_10
                                    lcl_10 = (rbnf_tmp_3 is None)
                                    if lcl_10:
                                        lcl_11 = builtin_tokens.offset
                                        lcl_11 = (lcl_11, 'quote ) not match')
                                        lcl_11 = builtin_cons(lcl_11, builtin_nil)
                                        lcl_11 = (False, lcl_11)
                                        lcl_10 = lcl_11
                                    else:
                                        lcl_11 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, String, rbnf_tmp_3, Type)
                                        rbnf_tmp_1_ = lcl_11
                                        lcl_11 = (True, rbnf_tmp_1_)
                                        lcl_10 = lcl_11
                                    lcl_8 = lcl_10
                                elif (lcl_9 == 6):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_10 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_10
                                    lcl_10 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                    rbnf_tmp_1_ = lcl_10
                                    lcl_10 = (True, rbnf_tmp_1_)
                                    lcl_8 = lcl_10
                                else:
                                    lcl_10 = (rbnf_named__off_2, 'lang_atom lookahead failed')
                                    lcl_10 = builtin_cons(lcl_10, builtin_nil)
                                    lcl_10 = (False, lcl_10)
                                    lcl_8 = lcl_10
                                lcl_7 = lcl_8
                            else:
                                lcl_10 = (rbnf_named__off_2, 'lang_atom got EOF')
                                lcl_10 = builtin_cons(lcl_10, builtin_nil)
                                lcl_10 = (False, lcl_10)
                                lcl_7 = lcl_10
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 6):
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_10 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_10
                        lcl_10 = ss(rbnf_tmp_0, Type, rbnf_tmp_1, Type)
                        rbnf_tmp_1_ = lcl_10
                        lcl_10 = (True, rbnf_tmp_1_)
                        lcl_4 = lcl_10
                    elif (lcl_5 == 5):
                        lcl_10 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_10
                        lcl_10 = rbnf_named__check_1[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_1
                        else:
                            lcl_11 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_7 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_7 = lcl_7.idint
                                if (lcl_7 == 0):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 6):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_8
                                    lcl_8 = (rbnf_tmp_3 is None)
                                    if lcl_8:
                                        lcl_9 = builtin_tokens.offset
                                        lcl_9 = (lcl_9, 'quote ) not match')
                                        lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                        lcl_9 = (False, lcl_9)
                                        lcl_8 = lcl_9
                                    else:
                                        lcl_9 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, String, rbnf_tmp_3, Type)
                                        rbnf_tmp_1_ = lcl_9
                                        lcl_9 = (True, rbnf_tmp_1_)
                                        lcl_8 = lcl_9
                                    lcl_6 = lcl_8
                                elif (lcl_7 == 6):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                    rbnf_tmp_1_ = lcl_8
                                    lcl_8 = (True, rbnf_tmp_1_)
                                    lcl_6 = lcl_8
                                else:
                                    lcl_8 = (rbnf_named__off_2, 'lang_atom lookahead failed')
                                    lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                    lcl_8 = (False, lcl_8)
                                    lcl_6 = lcl_8
                                lcl_11 = lcl_6
                            else:
                                lcl_6 = (rbnf_named__off_2, 'lang_atom got EOF')
                                lcl_6 = builtin_cons(lcl_6, builtin_nil)
                                lcl_6 = (False, lcl_6)
                                lcl_11 = lcl_6
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    elif (lcl_5 == 18):
                        lcl_10 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_10
                        lcl_10 = rbnf_named__check_1[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_1
                        else:
                            lcl_11 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_7 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_7 = lcl_7.idint
                                if (lcl_7 == 0):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 6):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_8
                                    lcl_8 = (rbnf_tmp_3 is None)
                                    if lcl_8:
                                        lcl_9 = builtin_tokens.offset
                                        lcl_9 = (lcl_9, 'quote ) not match')
                                        lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                        lcl_9 = (False, lcl_9)
                                        lcl_8 = lcl_9
                                    else:
                                        lcl_9 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, String, rbnf_tmp_3, Type)
                                        rbnf_tmp_1_ = lcl_9
                                        lcl_9 = (True, rbnf_tmp_1_)
                                        lcl_8 = lcl_9
                                    lcl_6 = lcl_8
                                elif (lcl_7 == 6):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                    rbnf_tmp_1_ = lcl_8
                                    lcl_8 = (True, rbnf_tmp_1_)
                                    lcl_6 = lcl_8
                                else:
                                    lcl_8 = (rbnf_named__off_2, 'lang_atom lookahead failed')
                                    lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                    lcl_8 = (False, lcl_8)
                                    lcl_6 = lcl_8
                                lcl_11 = lcl_6
                            else:
                                lcl_6 = (rbnf_named__off_2, 'lang_atom got EOF')
                                lcl_6 = builtin_cons(lcl_6, builtin_nil)
                                lcl_6 = (False, lcl_6)
                                lcl_11 = lcl_6
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    elif (lcl_5 == 17):
                        lcl_10 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_10
                        lcl_10 = rbnf_named__check_1[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_1
                        else:
                            lcl_11 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_7 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_7 = lcl_7.idint
                                if (lcl_7 == 0):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 6):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_8
                                    lcl_8 = (rbnf_tmp_3 is None)
                                    if lcl_8:
                                        lcl_9 = builtin_tokens.offset
                                        lcl_9 = (lcl_9, 'quote ) not match')
                                        lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                        lcl_9 = (False, lcl_9)
                                        lcl_8 = lcl_9
                                    else:
                                        lcl_9 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, String, rbnf_tmp_3, Type)
                                        rbnf_tmp_1_ = lcl_9
                                        lcl_9 = (True, rbnf_tmp_1_)
                                        lcl_8 = lcl_9
                                    lcl_6 = lcl_8
                                elif (lcl_7 == 6):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                    rbnf_tmp_1_ = lcl_8
                                    lcl_8 = (True, rbnf_tmp_1_)
                                    lcl_6 = lcl_8
                                else:
                                    lcl_8 = (rbnf_named__off_2, 'lang_atom lookahead failed')
                                    lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                    lcl_8 = (False, lcl_8)
                                    lcl_6 = lcl_8
                                lcl_11 = lcl_6
                            else:
                                lcl_6 = (rbnf_named__off_2, 'lang_atom got EOF')
                                lcl_6 = builtin_cons(lcl_6, builtin_nil)
                                lcl_6 = (False, lcl_6)
                                lcl_11 = lcl_6
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    elif (lcl_5 == 1):
                        lcl_10 = rbnf_named_parse_lang_lst(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_10
                        lcl_10 = rbnf_named__check_1[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_1
                        else:
                            lcl_11 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_7 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_7 = lcl_7.idint
                                if (lcl_7 == 0):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 6):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_8
                                    lcl_8 = (rbnf_tmp_3 is None)
                                    if lcl_8:
                                        lcl_9 = builtin_tokens.offset
                                        lcl_9 = (lcl_9, 'quote ) not match')
                                        lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                        lcl_9 = (False, lcl_9)
                                        lcl_8 = lcl_9
                                    else:
                                        lcl_9 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, String, rbnf_tmp_3, Type)
                                        rbnf_tmp_1_ = lcl_9
                                        lcl_9 = (True, rbnf_tmp_1_)
                                        lcl_8 = lcl_9
                                    lcl_6 = lcl_8
                                elif (lcl_7 == 6):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_8 = _rbnf_cur_token
                                    rbnf_tmp_2 = lcl_8
                                    lcl_8 = ss(rbnf_tmp_0, Type, rbnf_tmp_2, Type)
                                    rbnf_tmp_1_ = lcl_8
                                    lcl_8 = (True, rbnf_tmp_1_)
                                    lcl_6 = lcl_8
                                else:
                                    lcl_8 = (rbnf_named__off_2, 'lang_atom lookahead failed')
                                    lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                    lcl_8 = (False, lcl_8)
                                    lcl_6 = lcl_8
                                lcl_11 = lcl_6
                            else:
                                lcl_6 = (rbnf_named__off_2, 'lang_atom got EOF')
                                lcl_6 = builtin_cons(lcl_6, builtin_nil)
                                lcl_6 = (False, lcl_6)
                                lcl_11 = lcl_6
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    else:
                        lcl_10 = (rbnf_named__off_1, 'lang_atom lookahead failed')
                        lcl_10 = builtin_cons(lcl_10, builtin_nil)
                        lcl_10 = (False, lcl_10)
                        lcl_4 = lcl_10
                    lcl_3 = lcl_4
                else:
                    lcl_10 = (rbnf_named__off_1, 'lang_atom got EOF')
                    lcl_10 = builtin_cons(lcl_10, builtin_nil)
                    lcl_10 = (False, lcl_10)
                    lcl_3 = lcl_10
                lcl_1 = lcl_3
            elif (lcl_2 == 18):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_10 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_10
                try:
                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                    if (_rbnf_cur_token.idint is 17):
                        builtin_tokens.offset += 1
                    else:
                        _rbnf_cur_token = None
                except IndexError:
                    _rbnf_cur_token = None
                lcl_10 = _rbnf_cur_token
                rbnf_tmp_1 = lcl_10
                lcl_10 = (rbnf_tmp_1 is None)
                if lcl_10:
                    lcl_11 = builtin_tokens.offset
                    lcl_11 = (lcl_11, 'Int not match')
                    lcl_11 = builtin_cons(lcl_11, builtin_nil)
                    lcl_11 = (False, lcl_11)
                    lcl_10 = lcl_11
                else:
                    lcl_11 = s(rbnf_tmp_0, Call)
                    rbnf_tmp_1_ = lcl_11
                    lcl_11 = (True, rbnf_tmp_1_)
                    lcl_10 = lcl_11
                lcl_1 = lcl_10
            elif (lcl_2 == 17):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_10 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_10
                lcl_10 = s(rbnf_tmp_0, Literal)
                rbnf_tmp_1_ = lcl_10
                lcl_10 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_10
            elif (lcl_2 == 1):
                lcl_10 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                rbnf_named__check_0 = lcl_10
                lcl_10 = rbnf_named__check_0[0]
                lcl_10 = (lcl_10 == False)
                if lcl_10:
                    lcl_10 = rbnf_named__check_0
                else:
                    lcl_11 = rbnf_named__check_0[1]
                    rbnf_tmp_0 = lcl_11
                    lcl_11 = ()
                    rbnf_tmp_1_ = lcl_11
                    lcl_11 = (True, rbnf_tmp_1_)
                    lcl_10 = lcl_11
                lcl_1 = lcl_10
            else:
                lcl_10 = (rbnf_named__off_0, 'lang_atom lookahead failed')
                lcl_10 = builtin_cons(lcl_10, builtin_nil)
                lcl_10 = (False, lcl_10)
                lcl_1 = lcl_10
            lcl_0 = lcl_1
        else:
            lcl_1 = (rbnf_named__off_0, 'lang_atom got EOF')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_lang_lst(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_5(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_pragma(builtin_state, builtin_tokens):
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        try:
            builtin_tokens.array[(builtin_tokens.offset + 0)]
            _rbnf_peek_tmp = True
        except IndexError:
            _rbnf_peek_tmp = False
        lcl_0 = _rbnf_peek_tmp
        if lcl_0:
            lcl_2 = builtin_tokens.array[(builtin_tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 20):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = rbnf_named_parse_rbnfmacro_7(builtin_state, builtin_tokens)
                rbnf_named__check_1 = lcl_3
                lcl_3 = rbnf_named__check_1[0]
                lcl_3 = (lcl_3 == False)
                if lcl_3:
                    lcl_3 = rbnf_named__check_1
                else:
                    lcl_4 = rbnf_named__check_1[1]
                    rbnf_tmp_1 = lcl_4
                    lcl_4 = s(rbnf_tmp_0, Keyword)
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 19):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = builtin_tokens.offset
                rbnf_named__off_1 = lcl_3
                try:
                    builtin_tokens.array[(builtin_tokens.offset + 0)]
                    _rbnf_peek_tmp = True
                except IndexError:
                    _rbnf_peek_tmp = False
                lcl_3 = _rbnf_peek_tmp
                if lcl_3:
                    lcl_5 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                    lcl_5 = lcl_5.idint
                    if (lcl_5 == 2):
                        lcl_6 = rbnf_named_parse_rbnfmacro_6(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            lcl_7 = s(rbnf_tmp_0, Keyword)
                            rbnf_tmp_1_ = lcl_7
                            lcl_7 = (True, rbnf_tmp_1_)
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    elif (lcl_5 == 1):
                        lcl_6 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                        rbnf_named__check_1 = lcl_6
                        lcl_6 = rbnf_named__check_1[0]
                        lcl_6 = (lcl_6 == False)
                        if lcl_6:
                            lcl_6 = rbnf_named__check_1
                        else:
                            lcl_7 = rbnf_named__check_1[1]
                            rbnf_tmp_1 = lcl_7
                            lcl_7 = rbnf_named_parse_rbnfmacro_6(builtin_state, builtin_tokens)
                            rbnf_named__check_2 = lcl_7
                            lcl_7 = rbnf_named__check_2[0]
                            lcl_7 = (lcl_7 == False)
                            if lcl_7:
                                lcl_7 = rbnf_named__check_2
                            else:
                                lcl_8 = rbnf_named__check_2[1]
                                rbnf_tmp_2 = lcl_8
                                lcl_8 = s(rbnf_tmp_0, Keyword)
                                rbnf_tmp_1_ = lcl_8
                                lcl_8 = (True, rbnf_tmp_1_)
                                lcl_7 = lcl_8
                            lcl_6 = lcl_7
                        lcl_4 = lcl_6
                    else:
                        lcl_6 = (rbnf_named__off_1, 'pragma lookahead failed')
                        lcl_6 = builtin_cons(lcl_6, builtin_nil)
                        lcl_6 = (False, lcl_6)
                        lcl_4 = lcl_6
                    lcl_3 = lcl_4
                else:
                    lcl_4 = (rbnf_named__off_1, 'pragma got EOF')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 1):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                try:
                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                    if (_rbnf_cur_token.idint is 21):
                        builtin_tokens.offset += 1
                    else:
                        _rbnf_cur_token = None
                except IndexError:
                    _rbnf_cur_token = None
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_1 = lcl_3
                lcl_3 = (rbnf_tmp_1 is None)
                if lcl_3:
                    lcl_4 = builtin_tokens.offset
                    lcl_4 = (lcl_4, 'Code not match')
                    lcl_4 = builtin_cons(lcl_4, builtin_nil)
                    lcl_4 = (False, lcl_4)
                    lcl_3 = lcl_4
                else:
                    lcl_4 = ()
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_3 = lcl_4
                lcl_1 = lcl_3
            elif (lcl_2 == 21):
                _rbnf_old_offset = builtin_tokens.offset
                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                builtin_tokens.offset = (_rbnf_old_offset + 1)
                lcl_3 = _rbnf_cur_token
                rbnf_tmp_0 = lcl_3
                lcl_3 = ()
                rbnf_tmp_1_ = lcl_3
                lcl_3 = (True, rbnf_tmp_1_)
                lcl_1 = lcl_3
            else:
                lcl_3 = (rbnf_named__off_0, 'pragma lookahead failed')
                lcl_3 = builtin_cons(lcl_3, builtin_nil)
                lcl_3 = (False, lcl_3)
                lcl_1 = lcl_3
            lcl_0 = lcl_1
        else:
            lcl_1 = (rbnf_named__off_0, 'pragma got EOF')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_prod(builtin_state, builtin_tokens):
        lcl_0 = builtin_tokens.offset
        rbnf_named__off_0 = lcl_0
        try:
            builtin_tokens.array[(builtin_tokens.offset + 0)]
            _rbnf_peek_tmp = True
        except IndexError:
            _rbnf_peek_tmp = False
        lcl_0 = _rbnf_peek_tmp
        if lcl_0:
            lcl_2 = builtin_tokens.array[(builtin_tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 1):
                lcl_3 = builtin_tokens.offset
                rbnf_named__off_1 = lcl_3
                try:
                    builtin_tokens.array[(builtin_tokens.offset + 1)]
                    _rbnf_peek_tmp = True
                except IndexError:
                    _rbnf_peek_tmp = False
                lcl_3 = _rbnf_peek_tmp
                if lcl_3:
                    lcl_5 = builtin_tokens.array[(builtin_tokens.offset + 1)]
                    lcl_5 = lcl_5.idint
                    if (lcl_5 == 7):
                        lcl_6 = builtin_tokens.offset
                        rbnf_named__off_2 = lcl_6
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_0 = lcl_6
                        lcl_6 = builtin_tokens.offset
                        rbnf_named__off_3 = lcl_6
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_6 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_6
                        lcl_6 = builtin_tokens.offset
                        rbnf_named__off_4 = lcl_6
                        try:
                            builtin_tokens.array[(builtin_tokens.offset + 0)]
                            _rbnf_peek_tmp = True
                        except IndexError:
                            _rbnf_peek_tmp = False
                        lcl_6 = _rbnf_peek_tmp
                        if lcl_6:
                            lcl_8 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                            lcl_8 = lcl_8.idint
                            if (lcl_8 == 8):
                                _rbnf_old_offset = builtin_tokens.offset
                                _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                builtin_tokens.offset = (_rbnf_old_offset + 1)
                                lcl_9 = _rbnf_cur_token
                                rbnf_tmp_2 = lcl_9
                                try:
                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                    if (_rbnf_cur_token.idint is 14):
                                        builtin_tokens.offset += 1
                                    else:
                                        _rbnf_cur_token = None
                                except IndexError:
                                    _rbnf_cur_token = None
                                lcl_9 = _rbnf_cur_token
                                rbnf_tmp_3 = lcl_9
                                lcl_9 = (rbnf_tmp_3 is None)
                                if lcl_9:
                                    lcl_10 = builtin_tokens.offset
                                    lcl_10 = (lcl_10, 'quote := not match')
                                    lcl_10 = builtin_cons(lcl_10, builtin_nil)
                                    lcl_10 = (False, lcl_10)
                                    lcl_9 = lcl_10
                                else:
                                    lcl_10 = rbnf_named_parse_alts(builtin_state, builtin_tokens)
                                    rbnf_named__check_4 = lcl_10
                                    lcl_10 = rbnf_named__check_4[0]
                                    lcl_10 = (lcl_10 == False)
                                    if lcl_10:
                                        lcl_10 = rbnf_named__check_4
                                    else:
                                        lcl_11 = rbnf_named__check_4[1]
                                        rbnf_tmp_4 = lcl_11
                                        try:
                                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                            if (_rbnf_cur_token.idint is 15):
                                                builtin_tokens.offset += 1
                                            else:
                                                _rbnf_cur_token = None
                                        except IndexError:
                                            _rbnf_cur_token = None
                                        lcl_11 = _rbnf_cur_token
                                        rbnf_tmp_5 = lcl_11
                                        lcl_11 = (rbnf_tmp_5 is None)
                                        if lcl_11:
                                            lcl_12 = builtin_tokens.offset
                                            lcl_12 = (lcl_12, 'quote ; not match')
                                            lcl_12 = builtin_cons(lcl_12, builtin_nil)
                                            lcl_12 = (False, lcl_12)
                                            lcl_11 = lcl_12
                                        else:
                                            lcl_12 = s(rbnf_tmp_0, Pattern)
                                            rbnf_tmp_1_ = lcl_12
                                            lcl_12 = (True, rbnf_tmp_1_)
                                            lcl_11 = lcl_12
                                        lcl_10 = lcl_11
                                    lcl_9 = lcl_10
                                lcl_7 = lcl_9
                            elif (lcl_8 == 1):
                                lcl_10 = rbnf_named_parse_IdentList(builtin_state, builtin_tokens)
                                rbnf_named__check_2 = lcl_10
                                lcl_10 = rbnf_named__check_2[0]
                                lcl_10 = (lcl_10 == False)
                                if lcl_10:
                                    lcl_10 = rbnf_named__check_2
                                else:
                                    lcl_11 = rbnf_named__check_2[1]
                                    rbnf_tmp_2 = lcl_11
                                    try:
                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                        if (_rbnf_cur_token.idint is 8):
                                            builtin_tokens.offset += 1
                                        else:
                                            _rbnf_cur_token = None
                                    except IndexError:
                                        _rbnf_cur_token = None
                                    lcl_11 = _rbnf_cur_token
                                    rbnf_tmp_3 = lcl_11
                                    lcl_11 = (rbnf_tmp_3 is None)
                                    if lcl_11:
                                        lcl_12 = builtin_tokens.offset
                                        lcl_12 = (lcl_12, 'quote ] not match')
                                        lcl_12 = builtin_cons(lcl_12, builtin_nil)
                                        lcl_12 = (False, lcl_12)
                                        lcl_11 = lcl_12
                                    else:
                                        try:
                                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                            if (_rbnf_cur_token.idint is 14):
                                                builtin_tokens.offset += 1
                                            else:
                                                _rbnf_cur_token = None
                                        except IndexError:
                                            _rbnf_cur_token = None
                                        lcl_12 = _rbnf_cur_token
                                        rbnf_tmp_4 = lcl_12
                                        lcl_12 = (rbnf_tmp_4 is None)
                                        if lcl_12:
                                            lcl_9 = builtin_tokens.offset
                                            lcl_9 = (lcl_9, 'quote := not match')
                                            lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                            lcl_9 = (False, lcl_9)
                                            lcl_12 = lcl_9
                                        else:
                                            lcl_9 = rbnf_named_parse_alts(builtin_state, builtin_tokens)
                                            rbnf_named__check_5 = lcl_9
                                            lcl_9 = rbnf_named__check_5[0]
                                            lcl_9 = (lcl_9 == False)
                                            if lcl_9:
                                                lcl_9 = rbnf_named__check_5
                                            else:
                                                lcl_13 = rbnf_named__check_5[1]
                                                rbnf_tmp_5 = lcl_13
                                                try:
                                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                    if (_rbnf_cur_token.idint is 15):
                                                        builtin_tokens.offset += 1
                                                    else:
                                                        _rbnf_cur_token = None
                                                except IndexError:
                                                    _rbnf_cur_token = None
                                                lcl_13 = _rbnf_cur_token
                                                rbnf_tmp_6 = lcl_13
                                                lcl_13 = (rbnf_tmp_6 is None)
                                                if lcl_13:
                                                    lcl_14 = builtin_tokens.offset
                                                    lcl_14 = (lcl_14, 'quote ; not match')
                                                    lcl_14 = builtin_cons(lcl_14, builtin_nil)
                                                    lcl_14 = (False, lcl_14)
                                                    lcl_13 = lcl_14
                                                else:
                                                    lcl_14 = ss(rbnf_tmp_0, Pattern, rbnf_tmp_1, Call, rbnf_tmp_3, Call, rbnf_tmp_4, Keyword)
                                                    rbnf_tmp_1_ = lcl_14
                                                    lcl_14 = (True, rbnf_tmp_1_)
                                                    lcl_13 = lcl_14
                                                lcl_9 = lcl_13
                                            lcl_12 = lcl_9
                                        lcl_11 = lcl_12
                                    lcl_10 = lcl_11
                                lcl_7 = lcl_10
                            else:
                                lcl_10 = (rbnf_named__off_4, 'prod lookahead failed')
                                lcl_10 = builtin_cons(lcl_10, builtin_nil)
                                lcl_10 = (False, lcl_10)
                                lcl_7 = lcl_10
                            lcl_6 = lcl_7
                        else:
                            lcl_10 = (rbnf_named__off_4, 'prod got EOF')
                            lcl_10 = builtin_cons(lcl_10, builtin_nil)
                            lcl_10 = (False, lcl_10)
                            lcl_6 = lcl_10
                        lcl_4 = lcl_6
                    elif (lcl_5 == 16):
                        lcl_10 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                        rbnf_named__check_0 = lcl_10
                        lcl_10 = rbnf_named__check_0[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_0
                        else:
                            lcl_11 = rbnf_named__check_0[1]
                            rbnf_tmp_0 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_13 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_13 = lcl_13.idint
                                if (lcl_13 == 7):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_14 = _rbnf_cur_token
                                    rbnf_tmp_1 = lcl_14
                                    lcl_14 = builtin_tokens.offset
                                    rbnf_named__off_3 = lcl_14
                                    try:
                                        builtin_tokens.array[(builtin_tokens.offset + 0)]
                                        _rbnf_peek_tmp = True
                                    except IndexError:
                                        _rbnf_peek_tmp = False
                                    lcl_14 = _rbnf_peek_tmp
                                    if lcl_14:
                                        lcl_7 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                        lcl_7 = lcl_7.idint
                                        if (lcl_7 == 8):
                                            _rbnf_old_offset = builtin_tokens.offset
                                            _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                            builtin_tokens.offset = (_rbnf_old_offset + 1)
                                            lcl_8 = _rbnf_cur_token
                                            rbnf_tmp_2 = lcl_8
                                            try:
                                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                if (_rbnf_cur_token.idint is 16):
                                                    builtin_tokens.offset += 1
                                                else:
                                                    _rbnf_cur_token = None
                                            except IndexError:
                                                _rbnf_cur_token = None
                                            lcl_8 = _rbnf_cur_token
                                            rbnf_tmp_3 = lcl_8
                                            lcl_8 = (rbnf_tmp_3 is None)
                                            if lcl_8:
                                                lcl_9 = builtin_tokens.offset
                                                lcl_9 = (lcl_9, 'quote <=> not match')
                                                lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                                lcl_9 = (False, lcl_9)
                                                lcl_8 = lcl_9
                                            else:
                                                lcl_9 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                                rbnf_named__check_4 = lcl_9
                                                lcl_9 = rbnf_named__check_4[0]
                                                lcl_9 = (lcl_9 == False)
                                                if lcl_9:
                                                    lcl_9 = rbnf_named__check_4
                                                else:
                                                    lcl_15 = rbnf_named__check_4[1]
                                                    rbnf_tmp_4 = lcl_15
                                                    try:
                                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                        if (_rbnf_cur_token.idint is 15):
                                                            builtin_tokens.offset += 1
                                                        else:
                                                            _rbnf_cur_token = None
                                                    except IndexError:
                                                        _rbnf_cur_token = None
                                                    lcl_15 = _rbnf_cur_token
                                                    rbnf_tmp_5 = lcl_15
                                                    lcl_15 = (rbnf_tmp_5 is None)
                                                    if lcl_15:
                                                        lcl_16 = builtin_tokens.offset
                                                        lcl_16 = (lcl_16, 'quote ; not match')
                                                        lcl_16 = builtin_cons(lcl_16, builtin_nil)
                                                        lcl_16 = (False, lcl_16)
                                                        lcl_15 = lcl_16
                                                    else:
                                                        lcl_16 = ()
                                                        rbnf_tmp_1_ = lcl_16
                                                        lcl_16 = (True, rbnf_tmp_1_)
                                                        lcl_15 = lcl_16
                                                    lcl_9 = lcl_15
                                                lcl_8 = lcl_9
                                            lcl_6 = lcl_8
                                        elif (lcl_7 == 1):
                                            lcl_15 = rbnf_named_parse_IdentList(builtin_state, builtin_tokens)
                                            rbnf_named__check_2 = lcl_15
                                            lcl_15 = rbnf_named__check_2[0]
                                            lcl_15 = (lcl_15 == False)
                                            if lcl_15:
                                                lcl_15 = rbnf_named__check_2
                                            else:
                                                lcl_16 = rbnf_named__check_2[1]
                                                rbnf_tmp_2 = lcl_16
                                                try:
                                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                    if (_rbnf_cur_token.idint is 8):
                                                        builtin_tokens.offset += 1
                                                    else:
                                                        _rbnf_cur_token = None
                                                except IndexError:
                                                    _rbnf_cur_token = None
                                                lcl_16 = _rbnf_cur_token
                                                rbnf_tmp_3 = lcl_16
                                                lcl_16 = (rbnf_tmp_3 is None)
                                                if lcl_16:
                                                    lcl_8 = builtin_tokens.offset
                                                    lcl_8 = (lcl_8, 'quote ] not match')
                                                    lcl_8 = builtin_cons(lcl_8, builtin_nil)
                                                    lcl_8 = (False, lcl_8)
                                                    lcl_16 = lcl_8
                                                else:
                                                    try:
                                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                        if (_rbnf_cur_token.idint is 16):
                                                            builtin_tokens.offset += 1
                                                        else:
                                                            _rbnf_cur_token = None
                                                    except IndexError:
                                                        _rbnf_cur_token = None
                                                    lcl_8 = _rbnf_cur_token
                                                    rbnf_tmp_4 = lcl_8
                                                    lcl_8 = (rbnf_tmp_4 is None)
                                                    if lcl_8:
                                                        lcl_9 = builtin_tokens.offset
                                                        lcl_9 = (lcl_9, 'quote <=> not match')
                                                        lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                                        lcl_9 = (False, lcl_9)
                                                        lcl_8 = lcl_9
                                                    else:
                                                        lcl_9 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                                        rbnf_named__check_5 = lcl_9
                                                        lcl_9 = rbnf_named__check_5[0]
                                                        lcl_9 = (lcl_9 == False)
                                                        if lcl_9:
                                                            lcl_9 = rbnf_named__check_5
                                                        else:
                                                            lcl_17 = rbnf_named__check_5[1]
                                                            rbnf_tmp_5 = lcl_17
                                                            try:
                                                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                                if (_rbnf_cur_token.idint is 15):
                                                                    builtin_tokens.offset += 1
                                                                else:
                                                                    _rbnf_cur_token = None
                                                            except IndexError:
                                                                _rbnf_cur_token = None
                                                            lcl_17 = _rbnf_cur_token
                                                            rbnf_tmp_6 = lcl_17
                                                            lcl_17 = (rbnf_tmp_6 is None)
                                                            if lcl_17:
                                                                lcl_18 = builtin_tokens.offset
                                                                lcl_18 = (lcl_18, 'quote ; not match')
                                                                lcl_18 = builtin_cons(lcl_18, builtin_nil)
                                                                lcl_18 = (False, lcl_18)
                                                                lcl_17 = lcl_18
                                                            else:
                                                                lcl_18 = ()
                                                                rbnf_tmp_1_ = lcl_18
                                                                lcl_18 = (True, rbnf_tmp_1_)
                                                                lcl_17 = lcl_18
                                                            lcl_9 = lcl_17
                                                        lcl_8 = lcl_9
                                                    lcl_16 = lcl_8
                                                lcl_15 = lcl_16
                                            lcl_6 = lcl_15
                                        else:
                                            lcl_15 = (rbnf_named__off_3, 'prod lookahead failed')
                                            lcl_15 = builtin_cons(lcl_15, builtin_nil)
                                            lcl_15 = (False, lcl_15)
                                            lcl_6 = lcl_15
                                        lcl_14 = lcl_6
                                    else:
                                        lcl_15 = (rbnf_named__off_3, 'prod got EOF')
                                        lcl_15 = builtin_cons(lcl_15, builtin_nil)
                                        lcl_15 = (False, lcl_15)
                                        lcl_14 = lcl_15
                                    lcl_12 = lcl_14
                                elif (lcl_13 == 16):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_14 = _rbnf_cur_token
                                    rbnf_tmp_1 = lcl_14
                                    lcl_14 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                    rbnf_named__check_2 = lcl_14
                                    lcl_14 = rbnf_named__check_2[0]
                                    lcl_14 = (lcl_14 == False)
                                    if lcl_14:
                                        lcl_14 = rbnf_named__check_2
                                    else:
                                        lcl_15 = rbnf_named__check_2[1]
                                        rbnf_tmp_2 = lcl_15
                                        try:
                                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                            if (_rbnf_cur_token.idint is 15):
                                                builtin_tokens.offset += 1
                                            else:
                                                _rbnf_cur_token = None
                                        except IndexError:
                                            _rbnf_cur_token = None
                                        lcl_15 = _rbnf_cur_token
                                        rbnf_tmp_3 = lcl_15
                                        lcl_15 = (rbnf_tmp_3 is None)
                                        if lcl_15:
                                            lcl_16 = builtin_tokens.offset
                                            lcl_16 = (lcl_16, 'quote ; not match')
                                            lcl_16 = builtin_cons(lcl_16, builtin_nil)
                                            lcl_16 = (False, lcl_16)
                                            lcl_15 = lcl_16
                                        else:
                                            lcl_16 = ()
                                            rbnf_tmp_1_ = lcl_16
                                            lcl_16 = (True, rbnf_tmp_1_)
                                            lcl_15 = lcl_16
                                        lcl_14 = lcl_15
                                    lcl_12 = lcl_14
                                else:
                                    lcl_14 = (rbnf_named__off_2, 'prod lookahead failed')
                                    lcl_14 = builtin_cons(lcl_14, builtin_nil)
                                    lcl_14 = (False, lcl_14)
                                    lcl_12 = lcl_14
                                lcl_11 = lcl_12
                            else:
                                lcl_12 = (rbnf_named__off_2, 'prod got EOF')
                                lcl_12 = builtin_cons(lcl_12, builtin_nil)
                                lcl_12 = (False, lcl_12)
                                lcl_11 = lcl_12
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    elif (lcl_5 == 14):
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_10 = _rbnf_cur_token
                        rbnf_tmp_0 = lcl_10
                        lcl_10 = builtin_tokens.offset
                        rbnf_named__off_2 = lcl_10
                        _rbnf_old_offset = builtin_tokens.offset
                        _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                        builtin_tokens.offset = (_rbnf_old_offset + 1)
                        lcl_10 = _rbnf_cur_token
                        rbnf_tmp_1 = lcl_10
                        lcl_10 = rbnf_named_parse_alts(builtin_state, builtin_tokens)
                        rbnf_named__check_2 = lcl_10
                        lcl_10 = rbnf_named__check_2[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_2
                        else:
                            lcl_11 = rbnf_named__check_2[1]
                            rbnf_tmp_2 = lcl_11
                            try:
                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                if (_rbnf_cur_token.idint is 15):
                                    builtin_tokens.offset += 1
                                else:
                                    _rbnf_cur_token = None
                            except IndexError:
                                _rbnf_cur_token = None
                            lcl_11 = _rbnf_cur_token
                            rbnf_tmp_3 = lcl_11
                            lcl_11 = (rbnf_tmp_3 is None)
                            if lcl_11:
                                lcl_12 = builtin_tokens.offset
                                lcl_12 = (lcl_12, 'quote ; not match')
                                lcl_12 = builtin_cons(lcl_12, builtin_nil)
                                lcl_12 = (False, lcl_12)
                                lcl_11 = lcl_12
                            else:
                                lcl_12 = ss(rbnf_tmp_0, Var, rbnf_tmp_1, Keyword)
                                rbnf_tmp_1_ = lcl_12
                                lcl_12 = (True, rbnf_tmp_1_)
                                lcl_11 = lcl_12
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    else:
                        lcl_10 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
                        rbnf_named__check_0 = lcl_10
                        lcl_10 = rbnf_named__check_0[0]
                        lcl_10 = (lcl_10 == False)
                        if lcl_10:
                            lcl_10 = rbnf_named__check_0
                        else:
                            lcl_11 = rbnf_named__check_0[1]
                            rbnf_tmp_0 = lcl_11
                            lcl_11 = builtin_tokens.offset
                            rbnf_named__off_2 = lcl_11
                            try:
                                builtin_tokens.array[(builtin_tokens.offset + 0)]
                                _rbnf_peek_tmp = True
                            except IndexError:
                                _rbnf_peek_tmp = False
                            lcl_11 = _rbnf_peek_tmp
                            if lcl_11:
                                lcl_13 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                lcl_13 = lcl_13.idint
                                if (lcl_13 == 7):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_14 = _rbnf_cur_token
                                    rbnf_tmp_1 = lcl_14
                                    lcl_14 = builtin_tokens.offset
                                    rbnf_named__off_3 = lcl_14
                                    try:
                                        builtin_tokens.array[(builtin_tokens.offset + 0)]
                                        _rbnf_peek_tmp = True
                                    except IndexError:
                                        _rbnf_peek_tmp = False
                                    lcl_14 = _rbnf_peek_tmp
                                    if lcl_14:
                                        lcl_16 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                                        lcl_16 = lcl_16.idint
                                        if (lcl_16 == 8):
                                            _rbnf_old_offset = builtin_tokens.offset
                                            _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                            builtin_tokens.offset = (_rbnf_old_offset + 1)
                                            lcl_17 = _rbnf_cur_token
                                            rbnf_tmp_2 = lcl_17
                                            try:
                                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                if (_rbnf_cur_token.idint is 16):
                                                    builtin_tokens.offset += 1
                                                else:
                                                    _rbnf_cur_token = None
                                            except IndexError:
                                                _rbnf_cur_token = None
                                            lcl_17 = _rbnf_cur_token
                                            rbnf_tmp_3 = lcl_17
                                            lcl_17 = (rbnf_tmp_3 is None)
                                            if lcl_17:
                                                lcl_18 = builtin_tokens.offset
                                                lcl_18 = (lcl_18, 'quote <=> not match')
                                                lcl_18 = builtin_cons(lcl_18, builtin_nil)
                                                lcl_18 = (False, lcl_18)
                                                lcl_17 = lcl_18
                                            else:
                                                lcl_18 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                                rbnf_named__check_4 = lcl_18
                                                lcl_18 = rbnf_named__check_4[0]
                                                lcl_18 = (lcl_18 == False)
                                                if lcl_18:
                                                    lcl_18 = rbnf_named__check_4
                                                else:
                                                    lcl_6 = rbnf_named__check_4[1]
                                                    rbnf_tmp_4 = lcl_6
                                                    try:
                                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                        if (_rbnf_cur_token.idint is 15):
                                                            builtin_tokens.offset += 1
                                                        else:
                                                            _rbnf_cur_token = None
                                                    except IndexError:
                                                        _rbnf_cur_token = None
                                                    lcl_6 = _rbnf_cur_token
                                                    rbnf_tmp_5 = lcl_6
                                                    lcl_6 = (rbnf_tmp_5 is None)
                                                    if lcl_6:
                                                        lcl_7 = builtin_tokens.offset
                                                        lcl_7 = (lcl_7, 'quote ; not match')
                                                        lcl_7 = builtin_cons(lcl_7, builtin_nil)
                                                        lcl_7 = (False, lcl_7)
                                                        lcl_6 = lcl_7
                                                    else:
                                                        lcl_7 = ()
                                                        rbnf_tmp_1_ = lcl_7
                                                        lcl_7 = (True, rbnf_tmp_1_)
                                                        lcl_6 = lcl_7
                                                    lcl_18 = lcl_6
                                                lcl_17 = lcl_18
                                            lcl_15 = lcl_17
                                        elif (lcl_16 == 1):
                                            lcl_17 = rbnf_named_parse_IdentList(builtin_state, builtin_tokens)
                                            rbnf_named__check_2 = lcl_17
                                            lcl_17 = rbnf_named__check_2[0]
                                            lcl_17 = (lcl_17 == False)
                                            if lcl_17:
                                                lcl_17 = rbnf_named__check_2
                                            else:
                                                lcl_18 = rbnf_named__check_2[1]
                                                rbnf_tmp_2 = lcl_18
                                                try:
                                                    _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                    if (_rbnf_cur_token.idint is 8):
                                                        builtin_tokens.offset += 1
                                                    else:
                                                        _rbnf_cur_token = None
                                                except IndexError:
                                                    _rbnf_cur_token = None
                                                lcl_18 = _rbnf_cur_token
                                                rbnf_tmp_3 = lcl_18
                                                lcl_18 = (rbnf_tmp_3 is None)
                                                if lcl_18:
                                                    lcl_6 = builtin_tokens.offset
                                                    lcl_6 = (lcl_6, 'quote ] not match')
                                                    lcl_6 = builtin_cons(lcl_6, builtin_nil)
                                                    lcl_6 = (False, lcl_6)
                                                    lcl_18 = lcl_6
                                                else:
                                                    try:
                                                        _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                        if (_rbnf_cur_token.idint is 16):
                                                            builtin_tokens.offset += 1
                                                        else:
                                                            _rbnf_cur_token = None
                                                    except IndexError:
                                                        _rbnf_cur_token = None
                                                    lcl_6 = _rbnf_cur_token
                                                    rbnf_tmp_4 = lcl_6
                                                    lcl_6 = (rbnf_tmp_4 is None)
                                                    if lcl_6:
                                                        lcl_7 = builtin_tokens.offset
                                                        lcl_7 = (lcl_7, 'quote <=> not match')
                                                        lcl_7 = builtin_cons(lcl_7, builtin_nil)
                                                        lcl_7 = (False, lcl_7)
                                                        lcl_6 = lcl_7
                                                    else:
                                                        lcl_7 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                                        rbnf_named__check_5 = lcl_7
                                                        lcl_7 = rbnf_named__check_5[0]
                                                        lcl_7 = (lcl_7 == False)
                                                        if lcl_7:
                                                            lcl_7 = rbnf_named__check_5
                                                        else:
                                                            lcl_8 = rbnf_named__check_5[1]
                                                            rbnf_tmp_5 = lcl_8
                                                            try:
                                                                _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                                                if (_rbnf_cur_token.idint is 15):
                                                                    builtin_tokens.offset += 1
                                                                else:
                                                                    _rbnf_cur_token = None
                                                            except IndexError:
                                                                _rbnf_cur_token = None
                                                            lcl_8 = _rbnf_cur_token
                                                            rbnf_tmp_6 = lcl_8
                                                            lcl_8 = (rbnf_tmp_6 is None)
                                                            if lcl_8:
                                                                lcl_9 = builtin_tokens.offset
                                                                lcl_9 = (lcl_9, 'quote ; not match')
                                                                lcl_9 = builtin_cons(lcl_9, builtin_nil)
                                                                lcl_9 = (False, lcl_9)
                                                                lcl_8 = lcl_9
                                                            else:
                                                                lcl_9 = ()
                                                                rbnf_tmp_1_ = lcl_9
                                                                lcl_9 = (True, rbnf_tmp_1_)
                                                                lcl_8 = lcl_9
                                                            lcl_7 = lcl_8
                                                        lcl_6 = lcl_7
                                                    lcl_18 = lcl_6
                                                lcl_17 = lcl_18
                                            lcl_15 = lcl_17
                                        else:
                                            lcl_17 = (rbnf_named__off_3, 'prod lookahead failed')
                                            lcl_17 = builtin_cons(lcl_17, builtin_nil)
                                            lcl_17 = (False, lcl_17)
                                            lcl_15 = lcl_17
                                        lcl_14 = lcl_15
                                    else:
                                        lcl_15 = (rbnf_named__off_3, 'prod got EOF')
                                        lcl_15 = builtin_cons(lcl_15, builtin_nil)
                                        lcl_15 = (False, lcl_15)
                                        lcl_14 = lcl_15
                                    lcl_12 = lcl_14
                                elif (lcl_13 == 16):
                                    _rbnf_old_offset = builtin_tokens.offset
                                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                                    lcl_14 = _rbnf_cur_token
                                    rbnf_tmp_1 = lcl_14
                                    lcl_14 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
                                    rbnf_named__check_2 = lcl_14
                                    lcl_14 = rbnf_named__check_2[0]
                                    lcl_14 = (lcl_14 == False)
                                    if lcl_14:
                                        lcl_14 = rbnf_named__check_2
                                    else:
                                        lcl_15 = rbnf_named__check_2[1]
                                        rbnf_tmp_2 = lcl_15
                                        try:
                                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                                            if (_rbnf_cur_token.idint is 15):
                                                builtin_tokens.offset += 1
                                            else:
                                                _rbnf_cur_token = None
                                        except IndexError:
                                            _rbnf_cur_token = None
                                        lcl_15 = _rbnf_cur_token
                                        rbnf_tmp_3 = lcl_15
                                        lcl_15 = (rbnf_tmp_3 is None)
                                        if lcl_15:
                                            lcl_16 = builtin_tokens.offset
                                            lcl_16 = (lcl_16, 'quote ; not match')
                                            lcl_16 = builtin_cons(lcl_16, builtin_nil)
                                            lcl_16 = (False, lcl_16)
                                            lcl_15 = lcl_16
                                        else:
                                            lcl_16 = ()
                                            rbnf_tmp_1_ = lcl_16
                                            lcl_16 = (True, rbnf_tmp_1_)
                                            lcl_15 = lcl_16
                                        lcl_14 = lcl_15
                                    lcl_12 = lcl_14
                                else:
                                    lcl_14 = (rbnf_named__off_2, 'prod lookahead failed')
                                    lcl_14 = builtin_cons(lcl_14, builtin_nil)
                                    lcl_14 = (False, lcl_14)
                                    lcl_12 = lcl_14
                                lcl_11 = lcl_12
                            else:
                                lcl_12 = (rbnf_named__off_2, 'prod got EOF')
                                lcl_12 = builtin_cons(lcl_12, builtin_nil)
                                lcl_12 = (False, lcl_12)
                                lcl_11 = lcl_12
                            lcl_10 = lcl_11
                        lcl_4 = lcl_10
                    lcl_3 = lcl_4
                else:
                    lcl_10 = (rbnf_named__off_1, 'prod got EOF')
                    lcl_10 = builtin_cons(lcl_10, builtin_nil)
                    lcl_10 = (False, lcl_10)
                    lcl_3 = lcl_10
                lcl_1 = lcl_3
            else:
                lcl_10 = (rbnf_named__off_0, 'prod lookahead failed')
                lcl_10 = builtin_cons(lcl_10, builtin_nil)
                lcl_10 = (False, lcl_10)
                lcl_1 = lcl_10
            lcl_0 = lcl_1
        else:
            lcl_1 = (rbnf_named__off_0, 'prod got EOF')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_0(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_expr(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_0(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_1(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_atomExpr(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_1(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_2(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_cseq(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_2(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_3(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rewrite(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_3(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_4(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_4(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_5(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_lang(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_5(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_6(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_filename(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_6(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rbnfmacro_7(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_Ident(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = []
            _rbnf_immediate_lst = lcl_1
            _rbnf_immediate_lst.append(rbnf_tmp_0)
            lcl_1 = _rbnf_immediate_lst
            rbnf_tmp_1_ = lcl_1
            lcl_1 = rbnf_named_lr_loop_rbnfmacro_7(rbnf_tmp_1_, builtin_state, builtin_tokens)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_rewrite(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_seq(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = builtin_tokens.offset
            rbnf_named__off_0 = lcl_1
            try:
                builtin_tokens.array[(builtin_tokens.offset + 0)]
                _rbnf_peek_tmp = True
            except IndexError:
                _rbnf_peek_tmp = False
            lcl_1 = _rbnf_peek_tmp
            if lcl_1:
                lcl_3 = builtin_tokens.array[(builtin_tokens.offset + 0)]
                lcl_3 = lcl_3.idint
                if (lcl_3 == 12):
                    _rbnf_old_offset = builtin_tokens.offset
                    _rbnf_cur_token = builtin_tokens.array[_rbnf_old_offset]
                    builtin_tokens.offset = (_rbnf_old_offset + 1)
                    lcl_4 = _rbnf_cur_token
                    rbnf_tmp_1 = lcl_4
                    lcl_4 = rbnf_named_parse_lang(builtin_state, builtin_tokens)
                    rbnf_named__check_2 = lcl_4
                    lcl_4 = rbnf_named__check_2[0]
                    lcl_4 = (lcl_4 == False)
                    if lcl_4:
                        lcl_4 = rbnf_named__check_2
                    else:
                        lcl_5 = rbnf_named__check_2[1]
                        rbnf_tmp_2 = lcl_5
                        try:
                            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
                            if (_rbnf_cur_token.idint is 13):
                                builtin_tokens.offset += 1
                            else:
                                _rbnf_cur_token = None
                        except IndexError:
                            _rbnf_cur_token = None
                        lcl_5 = _rbnf_cur_token
                        rbnf_tmp_3 = lcl_5
                        lcl_5 = (rbnf_tmp_3 is None)
                        if lcl_5:
                            lcl_6 = builtin_tokens.offset
                            lcl_6 = (lcl_6, 'quote } not match')
                            lcl_6 = builtin_cons(lcl_6, builtin_nil)
                            lcl_6 = (False, lcl_6)
                            lcl_5 = lcl_6
                        else:
                            lcl_6 = ss(rbnf_tmp_1, String, rbnf_tmp_3, String)
                            rbnf_tmp_1_ = lcl_6
                            lcl_6 = (True, rbnf_tmp_1_)
                            lcl_5 = lcl_6
                        lcl_4 = lcl_5
                    lcl_2 = lcl_4
                else:
                    lcl_4 = ()
                    rbnf_tmp_1_ = lcl_4
                    lcl_4 = (True, rbnf_tmp_1_)
                    lcl_2 = lcl_4
                lcl_1 = lcl_2
            else:
                lcl_2 = (rbnf_named__off_0, 'rewrite got EOF')
                lcl_2 = builtin_cons(lcl_2, builtin_nil)
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_seq(builtin_state, builtin_tokens):
        lcl_0 = rbnf_named_parse_rbnfmacro_1(builtin_state, builtin_tokens)
        rbnf_named__check_0 = lcl_0
        lcl_0 = rbnf_named__check_0[0]
        lcl_0 = (lcl_0 == False)
        if lcl_0:
            lcl_0 = rbnf_named__check_0
        else:
            lcl_1 = rbnf_named__check_0[1]
            rbnf_tmp_0 = lcl_1
            lcl_1 = ()
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0

    def rbnf_named_parse_xor(builtin_state, builtin_tokens):
        try:
            _rbnf_cur_token = builtin_tokens.array[builtin_tokens.offset]
            if (_rbnf_cur_token.idint is 11):
                builtin_tokens.offset += 1
            else:
                _rbnf_cur_token = None
        except IndexError:
            _rbnf_cur_token = None
        lcl_0 = _rbnf_cur_token
        rbnf_tmp_0 = lcl_0
        lcl_0 = (rbnf_tmp_0 is None)
        if lcl_0:
            lcl_1 = builtin_tokens.offset
            lcl_1 = (lcl_1, 'quote | not match')
            lcl_1 = builtin_cons(lcl_1, builtin_nil)
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        else:
            lcl_1 = s(rbnf_tmp_0, String)
            rbnf_tmp_1_ = lcl_1
            lcl_1 = (True, rbnf_tmp_1_)
            lcl_0 = lcl_1
        return lcl_0
    return rbnf_named_parse_START