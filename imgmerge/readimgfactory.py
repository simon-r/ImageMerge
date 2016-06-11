# ImageMerge
# Copyright (C) 2012  Simone Riva mail: simone.rva {at} gmail {dot} com
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from imgmerge.readimg import ReadImageBasic, ReadImageRaw

class ReadImageFarctory( object ):
    def __init__(self):
        self._img_reads = [ ReadImageBasic() , ReadImageRaw() ]
        self._default_reader = self._img_reads[0]
        self._force_dafault = False

    def get_default_reader(self):
        return self._default_reader

    def set_default_reader(self, def_r):
        self._default_reader = def_r

    default_reader = property(get_default_reader, set_default_reader)

    def get_force_default(self):
        return self._force_dafault

    def set_force_dafault(self,f):
        self._force_dafault = f 

    force_default = property(get_force_default, set_force_dafault)

    def get_readimage(self, file_name=None):
        if not file_name or self.force_default:
            return self._default_reader

        for reader in self._img_reads :
            if reader.is_supported( file_name ):
                return reader

        return None

    
    