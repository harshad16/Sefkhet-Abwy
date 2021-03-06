#!/usr/bin/env python3
# sesheta-actions
# Copyright(C) 2019,2020 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Sesheta's actions."""


from .common import conclude_reviewer_list, unpack
from .label import do_not_merge
from .pull_request import local_check_gate_passed, needs_rebase_label, needs_approved_label, needs_size_label


__title__ = "sesheta-actions"
__version__ = "0.8.0"
