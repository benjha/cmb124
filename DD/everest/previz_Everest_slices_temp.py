# state file generated using paraview version 5.9.0-RC2

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1509, 677]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.00011597616326564498, -0.301658889736738, 0.04803624617492926]
renderView1.CameraFocalPoint = [-0.0009873558711804898, -0.22115822303986998, 0.02881541102712125]
renderView1.CameraViewUp = [-0.03017779900553348, 0.23174095269972703, 0.972309329014694]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.09852920780427725
renderView1.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView1.Background2 = [0.0, 0.0, 0.0]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.SamplesPerPixel = 16
renderView1.Denoise = 0
renderView1.TemporalCacheSize = 4
renderView1.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView1.EnvironmentEast = [0.0, 1.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1509, 677)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
pvpvd = PVDReader(registrationName='pv.pvd', FileName='/gpfs/alpine/proj-shared/cmb124/paraview_files/gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_16_cycle2/pv.pvd')
pvpvd.CellArrays = ['G_EQN_TRANSPORT', 'TEMPERATURE', 'velocity']

# create a new 'Extract Block'
cell_Slices = ExtractBlock(registrationName='Cell_Slices', Input=pvpvd)
cell_Slices.BlockIndices = [1]

# create a new 'Extract Block'
intakeExhaust_Geometry = ExtractBlock(registrationName='IntakeExhaust_Geometry', Input=pvpvd)
intakeExhaust_Geometry.BlockIndices = [6, 17, 7, 22, 23, 5, 20, 21, 8, 14, 15, 12, 13, 3, 19, 16]
intakeExhaust_Geometry.MaintainStructure = 1

# create a new 'Extract Block'
intake_Port = ExtractBlock(registrationName='Intake_Port', Input=intakeExhaust_Geometry)
intake_Port.BlockIndices = [7, 6, 9, 8, 10, 5]

# create a new 'Extract Block'
cell = ExtractBlock(registrationName='Cell', Input=pvpvd)
cell.BlockIndices = [1]

# create a new 'Stream Tracer'
intake_BackStreamTracer = StreamTracer(registrationName='Intake_BackStreamTracer', Input=cell,
    SeedType='Point Cloud')
intake_BackStreamTracer.Vectors = ['CELLS', 'velocity']
intake_BackStreamTracer.InitialStepLength = 0.1
intake_BackStreamTracer.MinimumStepLength = 0.09
intake_BackStreamTracer.MaximumStepLength = 0.9
intake_BackStreamTracer.MaximumStreamlineLength = 4.0
intake_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Cloud' selected for 'SeedType'
intake_BackStreamTracer.SeedType.Center = [0.0213827, 0.0187533, 0.0192229]
intake_BackStreamTracer.SeedType.NumberOfPoints = 10
intake_BackStreamTracer.SeedType.Radius = 0.022

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(registrationName='PythonAnnotation1', Input=cell)
pythonAnnotation1.Expression = '"CA %3.3f" % Crank_Angle[0]'

# create a new 'Extract Block'
intake_Geometry = ExtractBlock(registrationName='Intake_Geometry', Input=intakeExhaust_Geometry)
intake_Geometry.BlockIndices = [4, 7, 6, 9, 8, 10, 1, 3, 5]

# create a new 'Glyph'
intake_BackArrows = Glyph(registrationName='Intake_BackArrows', Input=intake_BackStreamTracer,
    GlyphType='Arrow')
intake_BackArrows.OrientationArray = ['POINTS', 'velocity']
intake_BackArrows.ScaleArray = ['POINTS', 'No scale array']
intake_BackArrows.ScaleFactor = 0.005
intake_BackArrows.GlyphTransform = 'Transform2'
intake_BackArrows.GlyphMode = 'Every Nth Point'
intake_BackArrows.MaximumNumberOfSamplePoints = 9000
intake_BackArrows.Seed = 5000
intake_BackArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
intake_BackArrows.GlyphType.TipRadius = 0.2

# create a new 'Stream Tracer'
exhaust_BackStreamTracer = StreamTracer(registrationName='Exhaust_BackStreamTracer', Input=cell,
    SeedType='Point Cloud')
exhaust_BackStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_BackStreamTracer.MinimumStepLength = 0.09
exhaust_BackStreamTracer.MaximumStepLength = 0.2
exhaust_BackStreamTracer.MaximumStreamlineLength = 4.0
exhaust_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Cloud' selected for 'SeedType'
exhaust_BackStreamTracer.SeedType.Center = [-0.0213827, 0.0187533, 0.0192229]
exhaust_BackStreamTracer.SeedType.NumberOfPoints = 10
exhaust_BackStreamTracer.SeedType.Radius = 0.02

# create a new 'Extract Block'
exhaust_Port = ExtractBlock(registrationName='Exhaust_Port', Input=intakeExhaust_Geometry)
exhaust_Port.BlockIndices = [11, 13, 12, 15, 14, 16]

# create a new 'Extract Block'
parcel = ExtractBlock(registrationName='Parcel', Input=pvpvd)
parcel.BlockIndices = [2]

# create a new 'Extract Block'
head = ExtractBlock(registrationName='Head', Input=intakeExhaust_Geometry)
head.BlockIndices = [1, 2]

# create a new 'Glyph'
exhaust_BackArrows = Glyph(registrationName='Exhaust_BackArrows', Input=exhaust_BackStreamTracer,
    GlyphType='Arrow')
exhaust_BackArrows.OrientationArray = ['POINTS', 'velocity']
exhaust_BackArrows.ScaleArray = ['POINTS', 'No scale array']
exhaust_BackArrows.ScaleFactor = 0.005
exhaust_BackArrows.GlyphTransform = 'Transform2'
exhaust_BackArrows.GlyphMode = 'Every Nth Point'
exhaust_BackArrows.MaximumNumberOfSamplePoints = 9000
exhaust_BackArrows.Seed = 5000
exhaust_BackArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
exhaust_BackArrows.GlyphType.TipRadius = 0.2

# create a new 'Extract Block'
plug = ExtractBlock(registrationName='Plug', Input=intake_Geometry)
plug.BlockIndices = [3, 2]

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=cell_Slices)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['CELLS', 'G_EQN_TRANSPORT']
clip1.Value = -0.10000009834766388

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.01486586358036437]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.08849244564771652, 0.000380881130695343, 0.05480236932635307]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=clip1)
cellDatatoPointData1.CellDataArraytoprocess = ['G_EQN_TRANSPORT', 'TEMPERATURE', 'velocity']

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=cellDatatoPointData1)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.001008335419341237, -0.0013291850130318127, 0.00023123608756124385]
slice2.SliceType.Normal = [-0.7071067811865476, -0.7071067811865476, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [0.08849244564771652, 0.000380881130695343, 0.05480236932635307]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=cellDatatoPointData1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0006219160003610295, 0.004378083999638971, 0.0]
slice1.SliceType.Normal = [-0.7071067811865476, 0.7071067811865476, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.08849244564771652, 0.000380881130695343, 0.05480236932635307]

# create a new 'Stream Tracer'
exhaust_FrontStreamTracer = StreamTracer(registrationName='Exhaust_FrontStreamTracer', Input=cell,
    SeedType='Point Cloud')
exhaust_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_FrontStreamTracer.MinimumStepLength = 0.09
exhaust_FrontStreamTracer.MaximumStepLength = 0.2
exhaust_FrontStreamTracer.MaximumStreamlineLength = 4.0
exhaust_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Cloud' selected for 'SeedType'
exhaust_FrontStreamTracer.SeedType.Center = [-0.0213827, -0.0187533, 0.0192229]
exhaust_FrontStreamTracer.SeedType.NumberOfPoints = 10
exhaust_FrontStreamTracer.SeedType.Radius = 0.02

# create a new 'Stream Tracer'
intake_FrontStreamTracer = StreamTracer(registrationName='Intake_FrontStreamTracer', Input=cell,
    SeedType='Point Cloud')
intake_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
intake_FrontStreamTracer.MinimumStepLength = 0.09
intake_FrontStreamTracer.MaximumStepLength = 0.2
intake_FrontStreamTracer.MaximumStreamlineLength = 4.0
intake_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Cloud' selected for 'SeedType'
intake_FrontStreamTracer.SeedType.Center = [0.021382743796776224, -0.01875330655923476, 0.019222949852495272]
intake_FrontStreamTracer.SeedType.NumberOfPoints = 10
intake_FrontStreamTracer.SeedType.Radius = 0.022

# create a new 'Glyph'
intake_FrontArrows = Glyph(registrationName='Intake_FrontArrows', Input=intake_FrontStreamTracer,
    GlyphType='Arrow')
intake_FrontArrows.OrientationArray = ['POINTS', 'velocity']
intake_FrontArrows.ScaleArray = ['POINTS', 'No scale array']
intake_FrontArrows.ScaleFactor = 0.005
intake_FrontArrows.GlyphTransform = 'Transform2'
intake_FrontArrows.GlyphMode = 'Every Nth Point'
intake_FrontArrows.MaximumNumberOfSamplePoints = 9000
intake_FrontArrows.Seed = 5000
intake_FrontArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
intake_FrontArrows.GlyphType.TipRadius = 0.2

# create a new 'Glyph'
exhaust_FrontArrows = Glyph(registrationName='Exhaust_FrontArrows', Input=exhaust_FrontStreamTracer,
    GlyphType='Arrow')
exhaust_FrontArrows.OrientationArray = ['POINTS', 'velocity']
exhaust_FrontArrows.ScaleArray = ['POINTS', 'No scale array']
exhaust_FrontArrows.ScaleFactor = 0.005
exhaust_FrontArrows.GlyphTransform = 'Transform2'
exhaust_FrontArrows.GlyphMode = 'Every Nth Point'
exhaust_FrontArrows.MaximumNumberOfSamplePoints = 9000
exhaust_FrontArrows.Seed = 5000
exhaust_FrontArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
exhaust_FrontArrows.GlyphType.TipRadius = 0.2

# create a new 'Cell Data to Point Data'
cell2Point_EQN_TRANS = CellDatatoPointData(registrationName='Cell2Point_EQN_TRANS', Input=cell)
cell2Point_EQN_TRANS.ProcessAllArrays = 0
cell2Point_EQN_TRANS.CellDataArraytoprocess = ['G_EQN_TRANSPORT']

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cell2Point_EQN_TRANS)
contour1.ContourBy = ['POINTS', 'G_EQN_TRANSPORT']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from plug
plugDisplay = Show(plug, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay.Representation = 'Surface'
plugDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay.ColorArrayName = ['POINTS', '']
plugDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay.Opacity = 0.7
plugDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay.SelectOrientationVectors = 'None'
plugDisplay.ScaleFactor = 0.020157745480537417
plugDisplay.SelectScaleArray = 'None'
plugDisplay.GlyphType = 'Arrow'
plugDisplay.GlyphTableIndexArray = 'None'
plugDisplay.GaussianRadius = 0.0010078872740268707
plugDisplay.SetScaleArray = [None, '']
plugDisplay.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay.OpacityArray = [None, '']
plugDisplay.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay.PolarAxes = 'PolarAxesRepresentation'
plugDisplay.ScalarOpacityUnitDistance = 0.002310755212500419
plugDisplay.OpacityArrayName = [None, '']
plugDisplay.ExtractedBlockIndex = 1

# show data from head
headDisplay = Show(head, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay.Representation = 'Surface'
headDisplay.ColorArrayName = [None, '']
headDisplay.Opacity = 0.3
headDisplay.SelectTCoordArray = 'None'
headDisplay.SelectNormalArray = 'None'
headDisplay.SelectTangentArray = 'None'
headDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
headDisplay.SelectOrientationVectors = 'None'
headDisplay.ScaleFactor = 0.008899322897195817
headDisplay.SelectScaleArray = 'None'
headDisplay.GlyphType = 'Arrow'
headDisplay.GlyphTableIndexArray = 'None'
headDisplay.GaussianRadius = 0.0004449661448597908
headDisplay.SetScaleArray = [None, '']
headDisplay.ScaleTransferFunction = 'PiecewiseFunction'
headDisplay.OpacityArray = [None, '']
headDisplay.OpacityTransferFunction = 'PiecewiseFunction'
headDisplay.DataAxesGrid = 'GridAxesRepresentation'
headDisplay.PolarAxes = 'PolarAxesRepresentation'
headDisplay.ScalarOpacityUnitDistance = 0.0016499601988645993
headDisplay.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
headDisplay.ExtractedBlockIndex = 1

# show data from intake_Port
intake_PortDisplay = Show(intake_Port, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_PortDisplay.Representation = 'Surface'
intake_PortDisplay.ColorArrayName = [None, '']
intake_PortDisplay.Opacity = 0.05
intake_PortDisplay.SelectTCoordArray = 'None'
intake_PortDisplay.SelectNormalArray = 'None'
intake_PortDisplay.SelectTangentArray = 'None'
intake_PortDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_PortDisplay.SelectOrientationVectors = 'None'
intake_PortDisplay.ScaleFactor = 0.013505461439490319
intake_PortDisplay.SelectScaleArray = 'None'
intake_PortDisplay.GlyphType = 'Arrow'
intake_PortDisplay.GlyphTableIndexArray = 'None'
intake_PortDisplay.GaussianRadius = 0.000675273071974516
intake_PortDisplay.SetScaleArray = [None, '']
intake_PortDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_PortDisplay.OpacityArray = [None, '']
intake_PortDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_PortDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_PortDisplay.PolarAxes = 'PolarAxesRepresentation'
intake_PortDisplay.ScalarOpacityUnitDistance = 0.0016352758047057535
intake_PortDisplay.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_PortDisplay.ExtractedBlockIndex = 1

# show data from exhaust_Port
exhaust_PortDisplay = Show(exhaust_Port, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_PortDisplay.Representation = 'Surface'
exhaust_PortDisplay.ColorArrayName = ['POINTS', '']
exhaust_PortDisplay.Opacity = 0.05
exhaust_PortDisplay.SelectTCoordArray = 'None'
exhaust_PortDisplay.SelectNormalArray = 'None'
exhaust_PortDisplay.SelectTangentArray = 'None'
exhaust_PortDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_PortDisplay.SelectOrientationVectors = 'None'
exhaust_PortDisplay.ScaleFactor = -2.0000000000000002e+298
exhaust_PortDisplay.SelectScaleArray = 'None'
exhaust_PortDisplay.GlyphType = 'Arrow'
exhaust_PortDisplay.GlyphTableIndexArray = 'None'
exhaust_PortDisplay.GaussianRadius = -1e+297
exhaust_PortDisplay.SetScaleArray = [None, '']
exhaust_PortDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_PortDisplay.OpacityArray = [None, '']
exhaust_PortDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_PortDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_PortDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'TEMPERATURE'
tEMPERATURELUT = GetColorTransferFunction('TEMPERATURE')
tEMPERATURELUT.RGBPoints = [363.859619140625, 0.0, 0.0, 0.0, 860.3128642578124, 0.501960784314, 0.0, 0.0, 1356.766109375, 1.0, 0.501960784314, 0.0, 1854.710205078125, 1.0, 1.0, 1.0]
tEMPERATURELUT.ColorSpace = 'RGB'
tEMPERATURELUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'TEMPERATURE']
slice1Display.LookupTable = tEMPERATURELUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'G_EQN_TRANSPORT'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.014805143326520921
slice1Display.SelectScaleArray = 'G_EQN_TRANSPORT'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
slice1Display.GaussianRadius = 0.0007402571663260461
slice1Display.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.1000036969780922, 0.0, 0.5, 0.0, -0.09999669343233109, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.1000036969780922, 0.0, 0.5, 0.0, -0.09999669343233109, 1.0, 0.5, 0.0]

# show data from slice2
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'TEMPERATURE']
slice2Display.LookupTable = tEMPERATURELUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'G_EQN_TRANSPORT'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.014905303344130517
slice2Display.SelectScaleArray = 'G_EQN_TRANSPORT'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
slice2Display.GaussianRadius = 0.0007452651672065258
slice2Display.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [-0.10000225901603699, 0.0, 0.5, 0.0, -0.09999669343233109, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [-0.10000225901603699, 0.0, 0.5, 0.0, -0.09999669343233109, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for tEMPERATURELUT in view renderView1
tEMPERATURELUTColorBar = GetScalarBar(tEMPERATURELUT, renderView1)
tEMPERATURELUTColorBar.WindowLocation = 'LowerLeftCorner'
tEMPERATURELUTColorBar.Position = [0.06270709078860172, 0.01756587202007528]
tEMPERATURELUTColorBar.Title = 'TEMPERATURE'
tEMPERATURELUTColorBar.ComponentTitle = ''
tEMPERATURELUTColorBar.TitleColor = [0.0, 0.0, 0.0]
tEMPERATURELUTColorBar.LabelColor = [0.0, 0.0, 0.0]
tEMPERATURELUTColorBar.AddRangeLabels = 0
tEMPERATURELUTColorBar.RangeLabelFormat = '%-#6.2e'
tEMPERATURELUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
tEMPERATURELUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
tEMPERATURELUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'TEMPERATURE'
tEMPERATUREPWF = GetOpacityTransferFunction('TEMPERATURE')
tEMPERATUREPWF.Points = [363.859619140625, 0.0, 0.5, 0.0, 1854.710205078125, 1.0, 0.5, 0.0]
tEMPERATUREPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(slice1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')