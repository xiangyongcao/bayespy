######################################################################
# Copyright (C) 2015 Jaakko Luttinen
#
# This file is licensed under Version 3.0 of the GNU General Public
# License. See LICENSE for a text of the license.
######################################################################

######################################################################
# This file is part of BayesPy.
#
# BayesPy is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# BayesPy is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BayesPy.  If not, see <http://www.gnu.org/licenses/>.
######################################################################

import numpy as np

from .expfamily import ExponentialFamily

        
class PDF(ExponentialFamily):
    """
    General node with arbitrary probability density function
    """

    # Sub-classes must over-write this
    _distribution = None

    def __init__(self, pdf, *parents, approximation=None, **kwargs):

        if approximation is not None:
            raise NotImplementedError() #self._distribution = approximation._constructor

        super().__init__(*parents,
                         dims=dims,
                         **kwargs)
