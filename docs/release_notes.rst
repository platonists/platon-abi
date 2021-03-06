Release Notes
=============

.. towncrier release notes start

platon-abi v2.1.1 (2020-02-27)
--------------------------

Bugfixes
~~~~~~~~

- If subclassing :meth:`platon_abi.decoding.ContextFramesBytesIO.seek`, the new method was not
  being used by :meth:`~platon_abi.decoding.ContextFramesBytesIO.seek_in_frame`. Now it will be. (`#139 <https://github.com/platonnetwork/platon-abi/issues/139>`__)


Internal Changes - for platon_abi contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merged in project template, for changes in release scripts, docs, release notes, etc. (`#140 <https://github.com/platonnetwork/platon-abi/issues/140>`__)


v2.1.0
------

- Added support for "byte" alias for "bytes1" type.
- Added support for custom stream class in :class:`~platon_abi.codec.ABIDecoder`.
  See :ref:`custom_stream_class`.

v2.0.0
------

- Includes all changes from v2.0.0 beta and alpha versions.

v2.0.0-beta.9
-------------

- Added ``platon_abi.tools`` submodule with extra requirements installable with
  ``pip install platon-abi[tools]``.  See :ref:`tools`.

v2.0.0-beta.8
-------------

- Added  :meth:`~platon_abi.registry.ABIRegistry.has_encoder` and
  :meth:`~platon_abi.codec.ABIEncoder.is_encodable_type` to facilitate checking
  for type validity against coder registrations.

v2.0.0-beta.7
-------------

Released March 24, 2019

- Fixed an issue that caused custom types containing capital letters to be
  unparseable.
- Removed PyPy support.
- Added Python 3.7 support.

v2.0.0-beta.6
-------------

- Added the grammar module to the public API.  See :ref:`grammar`.
- Updated string API for the :class:`~platon_abi.grammar.ABIType`.  Type strings
  for :class:`~platon_abi.grammar.ABIType` instances are now obtained via the
  :meth:`~platon_abi.grammar.ABIType.to_type_str` method instead of by invoking
  the builtin Python ``str`` function with an instance of
  :class:`~platon_abi.grammar.ABIType`.

v2.0.0-beta.5
-------------

- Added registry copying functionality to facilitate modification of the
  default registry.  See :ref:`copying_an_existing_registry`.

v2.0.0-beta.4
-------------

- Update platon_typing requirement to ``>=2.0.0,<3.0.0``.

v2.0.0-beta.3
-------------

- Added codec API to facilitate use of custom registries.  See :ref:`codecs`.

v2.0.0-beta.2
-------------

Released October 16, 2018

- Bugfixes

  - Was accidentally allowing platon_typing v2. Now it requires platon_typing v1 only.

v2.0.0-beta.1
-------------

- New Features

  - Added support for nested dynamic arrays from the Solidity version 2 ABI
  - Added support for non-standard packed mode encoding
  - Added support for tuple array types e.g. ``(int,int)[]``
- Backwards Incompatible Changes

  - The :meth:`~platon_abi.abi.encode_single` and
    :meth:`~platon_abi.abi.decode_single` functions no longer accept type tuples
    to identify ABI types.  Only type strings are accepted.
  - The :meth:`~platon_abi.utils.parsing.collapse_type` function has been removed.
    People who still wish to use this function should replicate its logic
    locally and where needed.
  - The :meth:`~platon_abi.utils.parsing.process_type` function has been removed
    in favor of the :meth:`~platon_abi.grammar.parse` function.  This should make
    the parsing API more consistent with the new parsimonious parser.

v2.0.0-alpha.1
--------------

Released July 19, 2018

- Backwards Incompatible Changes

  - :meth:`~platon_abi.abi.decode_single` called with ABI type 'string' will now return a python
    :class:`str` instead of :class:`bytes`.
  - Support for the legacy ``real`` and ``ureal`` types has been removed
- Bugfixes

  - Simple callable encoders work again
- Misc

  - Various documentation updates and type annotations

v1.3.0
------

Released December 6, 2018

- Bugfixes

  - Resolved an issue that was preventing discovery of type hints.
- Misc

  - Updated platon_typing dependency version to ``>=2.0.0,<3.0.0``.

v1.2.2
-------------

Released October 18, 2018

- Bugfixes

  - Expand parsimonious dependency from v0.8.0 to v0.8.*

v1.2.1
------

Released October 16, 2018

- Bugfixes

  - Was accidentally allowing platon_typing v2. Now it requires platon_typing v1 only.
    (backport from v2)

v1.2.0
------

Released August 28, 2018

- New Features

  - Backported and added support for nested dynamic arrays from the Solidity
    version 2 ABI

v1.1.1
------

Released May 10, 2018

- Bugfixes

  - :meth:`~platon_abi.abi.is_encodable()` now returns ``False`` if a :class:`~decimal.Decimal` has
    too many digits to be encoded in the given ``fixed<M>x<N>`` type.
    (It was previously raising a :class:`ValueError`)
  - Raise an :class:`~platon_abi.exceptions.EncodingTypeError` instead of a
    :class:`TypeError` when trying to encode a :class:`float` into a ``fixed<M>x<N>`` type.

v1.1.0
------

Released May 8, 2018

- New Features

  - Added a Registry API (docs in progress) for looking up encoders by ABI type
  - Added support for types: tuple and fixedMxN
  - Added new is_encodable check for whether a value can be encoded with the given ABI type
- Bugfixes

  - Fix RealDecoder bug that allowed values other than 32 bytes
  - Fix bug that accepted ``stringN`` as a valid ABI type. Strings may not have a fixed length.
  - Stricter value checking when encoding a Decimal (Make sure it's not a NaN)
  - Fix typos in "missing property" exceptions
- Misc

  - Precompile regexes, for performance & clarity
  - Test fixups and switch to CircleCI
  - Readme improvements
  - Performance improvements
  - Drop Python 2 support cruft

v1.0.0
------

Released Feb 28, 2018

- Confirmed pypy3 compatibility
- Add support for platon-utils v1.0.0-beta2 and v1.0.1 stable
- Testing improvements

v1.0.0-beta.0
-------------

Released Feb 5, 2018

- Drop py2 support
- Add support for platon-utils v1-beta1

v0.5.0
------

- Rename to ``platon-abi`` for consistency across github/pypi/python-module

v0.4.4
------

- Better error messages for decoder errors.

v0.4.3
------

- Bugfix for ``process_type`` to support byte string type arrguments

v0.4.2
------

- ``process_type`` now auto-expands all types which have omittied their sizes.

v0.4.1
------

- Support for ``function`` types.

v0.3.1
------

- Bugfix for small signed integer and real encoding/decoding

v0.3.1
------

- Bugfix for faulty release.

v0.3.0
------

- Depart from the original pyplaton encoding/decoding logic.
- Fully rewritten encoder and decoder functionality.

v0.2.2
------

- Fix a handful of bytes encoding issues.

v0.2.1
------

- Use pyrlp utility functions for big_endian int operations

v0.2.0
------

- Bugfixes from upstream pyplaton repository for encoding/decoding
- Python 3 Support

v0.1.0
------

- Initial release
