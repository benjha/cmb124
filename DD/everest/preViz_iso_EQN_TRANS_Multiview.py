# state file generated using paraview version 5.8.1-1321-g16b5f10c4e

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

filename = 'iso_EQN_parcel_Multiview_' + str(sys.argv[1]).zfill(4) + '.png'
dt = int(sys.argv[1])
n_streams = 250
arrow_stride = 100

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [940, 548]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.04346333293059141, -0.380329863505669, -0.03570600265444192]
renderView1.CameraFocalPoint = [-0.04346333293059141, 0.0, -0.03570600265444192]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.08166297494027437
renderView1.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView1.Background2 = [0.0, 0.0, 0.0]
renderView1.EnableRayTracing = 1
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.SamplesPerPixel = 16
renderView1.Denoise = 0
renderView1.TemporalCacheSize = 4
renderView1.EnvironmentNorth = [1.0, 0.0, 0.0]
renderView1.EnvironmentEast = [0.0, 1.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [938, 530]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-0.04840901296123797, -0.6737775533219668, -0.0330060446156768]
renderView2.CameraFocalPoint = [-0.04840901296123797, 0.0, -0.0330060446156768]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 0.08065613493356827
renderView2.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView2.EnableRayTracing = 1
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.SamplesPerPixel = 16
renderView2.Denoise = 0
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [402, 548]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [-0.5067509234783554, -0.0004630845961597547, -0.02799105845096824]
renderView3.CameraFocalPoint = [0.04728114977478981, -0.0004630845961597547, -0.02799105845096824]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 0.08025393419951785
renderView3.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView3.EnableRayTracing = 1
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.SamplesPerPixel = 16
renderView3.Denoise = 0
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [574, 548]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [0.0029265009251664086, -0.0003718520223185817, 0.18161212738187246]
renderView4.CameraFocalPoint = [0.0029265009251664086, -0.0003718520223185817, -0.03199122058960833]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 0.04568976409312404
renderView4.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView4.EnableRayTracing = 1
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.SamplesPerPixel = 16
renderView4.Denoise = 0
renderView4.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [406, 530]
renderView5.InteractionMode = '2D'
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [0.04753166437149048, 5.289912223815918e-07, -0.004494160413742065]
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraPosition = [-0.505290897268397, -0.0017224683128397728, -0.03249286660475206]
renderView5.CameraFocalPoint = [0.04753166437149048, -0.0017224683128397728, -0.03249286660475206]
renderView5.CameraViewUp = [0.0, 0.0, 1.0]
renderView5.CameraFocalDisk = 1.0
renderView5.CameraParallelScale = 0.08076549862791348
renderView5.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView5.EnableRayTracing = 1
renderView5.BackEnd = 'OSPRay raycaster'
renderView5.SamplesPerPixel = 16
renderView5.Denoise = 0
renderView5.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.ViewSize = [572, 530]
renderView6.InteractionMode = '2D'
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.OrientationAxesVisibility = 0
renderView6.CenterOfRotation = [0.04753166437149048, 5.289912223815918e-07, -0.004494160413742065]
renderView6.StereoType = 'Crystal Eyes'
renderView6.CameraPosition = [0.0015842202038009194, -0.00021587162955998424, 0.20864286847176003]
renderView6.CameraFocalPoint = [0.0015842202038009194, -0.00021587162955998424, -0.004494160413742065]
renderView6.CameraFocalDisk = 1.0
renderView6.CameraParallelScale = 0.04559001842325126
renderView6.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView6.EnableRayTracing = 1
renderView6.BackEnd = 'OSPRay raycaster'
renderView6.SamplesPerPixel = 16
renderView6.Denoise = 0
renderView6.TemporalCacheSize = 4
renderView6.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.507229)
layout1.SplitHorizontal(1, 0.489493)
layout1.AssignView(3, renderView1)
layout1.SplitHorizontal(4, 0.410693)
layout1.AssignView(9, renderView3)
layout1.AssignView(10, renderView4)
layout1.SplitHorizontal(2, 0.488875)
layout1.AssignView(5, renderView2)
layout1.SplitHorizontal(6, 0.415049)
layout1.AssignView(13, renderView5)
layout1.AssignView(14, renderView6)
layout1.SetSize(1918, 1079)

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

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(Input=pvpvd)
extractTimeSteps1.TimeStepIndices = [dt]


# create a new 'Extract Block'
intakeExhaust_Geometry = ExtractBlock(registrationName='IntakeExhaust_Geometry', Input=extractTimeSteps1)
intakeExhaust_Geometry.BlockIndices = [8, 7, 6, 23, 5, 22, 21, 3, 20, 19, 17, 15, 16, 14, 13, 12]
intakeExhaust_Geometry.MaintainStructure = 1

# create a new 'Extract Block'
head = ExtractBlock(registrationName='Head', Input=intakeExhaust_Geometry)
head.BlockIndices = [2]

# create a new 'Extract Block'
intake_Geometry = ExtractBlock(registrationName='Intake_Geometry', Input=intakeExhaust_Geometry)
intake_Geometry.BlockIndices = [8, 7, 6, 5, 4, 3, 1, 10, 9]

# create a new 'Extract Block'
plug = ExtractBlock(registrationName='Plug', Input=intake_Geometry)
plug.BlockIndices = [3, 2]

# create a new 'Extract Block'
parcel = ExtractBlock(registrationName='Parcel', Input=extractTimeSteps1)
parcel.BlockIndices = [2]

# create a new 'Extract Block'
cell = ExtractBlock(registrationName='Cell', Input=extractTimeSteps1)
cell.BlockIndices = [1]

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(registrationName='PythonAnnotation1', Input=cell)
pythonAnnotation1.Expression = '"CA %3.3f" % Crank_Angle[0]'

# create a new 'Cell Data to Point Data'
cell2Point_EQN_TRANS = CellDatatoPointData(registrationName='Cell2Point_EQN_TRANS', Input=cell)
cell2Point_EQN_TRANS.ProcessAllArrays = 0
cell2Point_EQN_TRANS.CellDataArraytoprocess = ['G_EQN_TRANSPORT']

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
intake_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
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
intake_FrontArrows.Stride = arrow_stride 

# init the 'Arrow' selected for 'GlyphType'
intake_FrontArrows.GlyphType.TipRadius = 0.2

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
exhaust_BackStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_BackStreamTracer.SeedType.Radius = 0.02

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
exhaust_BackArrows.Stride = arrow_stride

# init the 'Arrow' selected for 'GlyphType'
exhaust_BackArrows.GlyphType.TipRadius = 0.2

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
intake_BackStreamTracer.SeedType.NumberOfPoints = n_streams
intake_BackStreamTracer.SeedType.Radius = 0.022

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
intake_BackArrows.Stride = arrow_stride

# init the 'Arrow' selected for 'GlyphType'
intake_BackArrows.GlyphType.TipRadius = 0.2

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
exhaust_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_FrontStreamTracer.SeedType.Radius = 0.02

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
exhaust_FrontArrows.Stride = arrow_stride

# init the 'Arrow' selected for 'GlyphType'
exhaust_FrontArrows.GlyphType.TipRadius = 0.2

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cell2Point_EQN_TRANS)
contour1.ContourBy = ['POINTS', 'G_EQN_TRANSPORT']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay = Show(intakeExhaust_Geometry, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay.Representation = 'Surface'
intakeExhaust_GeometryDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay.ColorArrayName = ['POINTS', '']
intakeExhaust_GeometryDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay.Opacity = 0.25
intakeExhaust_GeometryDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay.ScaleFactor = 0.010390702914446593
intakeExhaust_GeometryDisplay.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay.GaussianRadius = 0.0005195351457223296
intakeExhaust_GeometryDisplay.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay.ScalarOpacityUnitDistance = 0.001630907728715554
intakeExhaust_GeometryDisplay.OpacityArrayName = [None, '']
intakeExhaust_GeometryDisplay.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay = Show(intake_FrontStreamTracer, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.AutomaticRescaleRangeMode = 'Never'
velocityLUT.RGBPoints = [0.0, 0.6705882352941176, 0.6705882352941176, 0.6705882352941176, 15.566036975078656, 1.0, 0.6666666666666666, 0.0, 33.96226539099357, 1.0, 0.6666666666666666, 0.0, 61.320752879971984, 0.0, 0.615686274509804, 0.0, 87.2641478384364, 0.06274509803921569, 0.7372549019607844, 1.0, 113.67924030707218, 0.6666666666666666, 0.0, 0.0, 150.0, 1.0, 0.0, 0.0]
velocityLUT.NumberOfTableValues = 6
velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay.Representation = 'Surface'
intake_FrontStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_FrontStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.SelectOrientationVectors = 'Normals'
intake_FrontStreamTracerDisplay.ScaleFactor = 0.01835412085056305
intake_FrontStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
intake_FrontStreamTracerDisplay.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_FrontStreamTracerDisplay.GaussianRadius = 0.0009177060425281525
intake_FrontStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_FrontStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_FrontStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay = Show(intake_BackStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay.Representation = 'Surface'
intake_BackStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay.LookupTable = velocityLUT
intake_BackStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.SelectOrientationVectors = 'Normals'
intake_BackStreamTracerDisplay.ScaleFactor = 0.003236056445166469
intake_BackStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.GaussianRadius = 0.00016180282225832342
intake_BackStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_BackStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_BackStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from intake_FrontArrows
intake_FrontArrowsDisplay = Show(intake_FrontArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay.Representation = 'Surface'
intake_FrontArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_FrontArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
intake_FrontArrowsDisplay.ScaleFactor = 13.32074661254883
intake_FrontArrowsDisplay.SelectScaleArray = 'AngularVelocity'
intake_FrontArrowsDisplay.GlyphType = 'Arrow'
intake_FrontArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_FrontArrowsDisplay.GaussianRadius = 0.6660373306274414
intake_FrontArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_FrontArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_FrontArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from intake_BackArrows
intake_BackArrowsDisplay = Show(intake_BackArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay.Representation = 'Surface'
intake_BackArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay.ColorArrayName = ['POINTS', '']
intake_BackArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_BackArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
intake_BackArrowsDisplay.ScaleFactor = 0.017043457902962456
intake_BackArrowsDisplay.SelectScaleArray = 'AngularVelocity'
intake_BackArrowsDisplay.GlyphType = 'Arrow'
intake_BackArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_BackArrowsDisplay.GaussianRadius = 0.0008521728951481228
intake_BackArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_BackArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_BackArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay = Show(exhaust_FrontStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay.Representation = 'Surface'
exhaust_FrontStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.SelectOrientationVectors = 'Normals'
exhaust_FrontStreamTracerDisplay.ScaleFactor = 0.00614069551229477
exhaust_FrontStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.GaussianRadius = 0.0003070347756147385
exhaust_FrontStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
exhaust_FrontStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
exhaust_FrontStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay = Show(exhaust_FrontArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay.Representation = 'Surface'
exhaust_FrontArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay.ColorArrayName = ['POINTS', '']
exhaust_FrontArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
exhaust_FrontArrowsDisplay.ScaleFactor = 0.0183842733502388
exhaust_FrontArrowsDisplay.SelectScaleArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.GaussianRadius = 0.00091921366751194
exhaust_FrontArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
exhaust_FrontArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
exhaust_FrontArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from pythonAnnotation1
pythonAnnotation1Display = Show(pythonAnnotation1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
pythonAnnotation1Display.Color = [0.0, 0.0, 0.0]
pythonAnnotation1Display.FontSize = 11
pythonAnnotation1Display.Position = [0.01, 0.9417426273458445]

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUT = GetColorTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTLUT.RGBPoints = [-0.10000014305114746, 0.050383, 0.029803, 0.527975, -0.09960794249010085, 0.063536, 0.028426, 0.533124, -0.09921584192919732, 0.075353, 0.027206, 0.538007, -0.09882364136815071, 0.086222, 0.026125, 0.542658, -0.09843154080724716, 0.096379, 0.025165, 0.547103, -0.09803934024620056, 0.10598, 0.024309, 0.551368, -0.09764723968529701, 0.115124, 0.023556, 0.555468, -0.09725503912425042, 0.123903, 0.022878, 0.559423, -0.09686283856320381, 0.132381, 0.022258, 0.56325, -0.09647073800230026, 0.140603, 0.021687, 0.566959, -0.09607853744125366, 0.148607, 0.021154, 0.570562, -0.09568643688035011, 0.156421, 0.020651, 0.574065, -0.09529423631930352, 0.16407, 0.020171, 0.577478, -0.09490213575839997, 0.171574, 0.019706, 0.580806, -0.09450993519735336, 0.17895, 0.019252, 0.584054, -0.09411773463630677, 0.186213, 0.018803, 0.587228, -0.09372563407540321, 0.193374, 0.018354, 0.59033, -0.0933334335143566, 0.200445, 0.017902, 0.593364, -0.09294133295345307, 0.207435, 0.017442, 0.596333, -0.09254913239240646, 0.21435, 0.016973, 0.599239, -0.09215703183150291, 0.221197, 0.016497, 0.602083, -0.09176483127045632, 0.227983, 0.016007, 0.604867, -0.09137263070940971, 0.234715, 0.015502, 0.607592, -0.09098053014850617, 0.241396, 0.014979, 0.610259, -0.09058832958745956, 0.248032, 0.014439, 0.612868, -0.09019622902655601, 0.254627, 0.013882, 0.615419, -0.08980402846550942, 0.261183, 0.013308, 0.617911, -0.08941192790460586, 0.267703, 0.012716, 0.620346, -0.08901972734355927, 0.274191, 0.012109, 0.622722, -0.08862762678265572, 0.280648, 0.011488, 0.625038, -0.08823542622160911, 0.287076, 0.010855, 0.627295, -0.08784322566056252, 0.293478, 0.010213, 0.62949, -0.08745112509965897, 0.299855, 0.009561, 0.631624, -0.08705892453861236, 0.30621, 0.008902, 0.633694, -0.08666682397770882, 0.312543, 0.008239, 0.6357, -0.08627462341666221, 0.318856, 0.007576, 0.63764, -0.08588252285575868, 0.32515, 0.006915, 0.639512, -0.08549032229471207, 0.331426, 0.006261, 0.641316, -0.08509812173366546, 0.337683, 0.005618, 0.643049, -0.08470602117276192, 0.343925, 0.004991, 0.64471, -0.08431382061171531, 0.35015, 0.004382, 0.646298, -0.08392172005081176, 0.356359, 0.003798, 0.64781, -0.08352951948976517, 0.362553, 0.003243, 0.649245, -0.08313741892886162, 0.368733, 0.002724, 0.650601, -0.08274521836781501, 0.374897, 0.002245, 0.651876, -0.08235301780676842, 0.381047, 0.001814, 0.653068, -0.08196091724586486, 0.387183, 0.001434, 0.654177, -0.08156871668481827, 0.393304, 0.001114, 0.655199, -0.08117661612391472, 0.399411, 0.000859, 0.656133, -0.08078441556286811, 0.405503, 0.000678, 0.656977, -0.08039231500196457, 0.41158, 0.000577, 0.65773, -0.08000011444091797, 0.417642, 0.000564, 0.65839, -0.07960791387987137, 0.423689, 0.000646, 0.658956, -0.07921581331896782, 0.429719, 0.000831, 0.659425, -0.07882361275792121, 0.435734, 0.001127, 0.659797, -0.07843151219701767, 0.441732, 0.00154, 0.660069, -0.07803931163597107, 0.447714, 0.00208, 0.66024, -0.07764721107506752, 0.453677, 0.002755, 0.66031, -0.07725501051402092, 0.459623, 0.003574, 0.660277, -0.07686280995297431, 0.46555, 0.004545, 0.660139, -0.07647070939207076, 0.471457, 0.005678, 0.659897, -0.07607850883102417, 0.477344, 0.00698, 0.659549, -0.07568640827012062, 0.48321, 0.00846, 0.659095, -0.07529420770907402, 0.489055, 0.010127, 0.658534, -0.07490210714817047, 0.494877, 0.01199, 0.657865, -0.07450990658712386, 0.500678, 0.014055, 0.657088, -0.07411770602607727, 0.506454, 0.016333, 0.656202, -0.07372560546517372, 0.512206, 0.018833, 0.655209, -0.07333340490412713, 0.517933, 0.021563, 0.654109, -0.07294130434322357, 0.523633, 0.024532, 0.652901, -0.07254910378217697, 0.529306, 0.027747, 0.651586, -0.07215700322127343, 0.534952, 0.031217, 0.650165, -0.07176480266022682, 0.54057, 0.03495, 0.64864, -0.07137260209918023, 0.546157, 0.038954, 0.64701, -0.07098050153827667, 0.551715, 0.043136, 0.645277, -0.07058830097723007, 0.557243, 0.047331, 0.643443, -0.07019620041632652, 0.562738, 0.051545, 0.641509, -0.06980399985527992, 0.568201, 0.055778, 0.639477, -0.06941189929437637, 0.573632, 0.060028, 0.637349, -0.06901969873332978, 0.579029, 0.064296, 0.635126, -0.06862759817242622, 0.584391, 0.068579, 0.632812, -0.06823539761137962, 0.589719, 0.072878, 0.630408, -0.06784319705033302, 0.595011, 0.07719, 0.627917, -0.06745109648942947, 0.600266, 0.081516, 0.625342, -0.06705889592838288, 0.605485, 0.085854, 0.622686, -0.06666679536747933, 0.610667, 0.090204, 0.619951, -0.06627459480643272, 0.615812, 0.094564, 0.61714, -0.06588249424552918, 0.620919, 0.098934, 0.614257, -0.06549029368448257, 0.625987, 0.103312, 0.611305, -0.06509809312343598, 0.631017, 0.107699, 0.608287, -0.06470599256253243, 0.636008, 0.112092, 0.605205, -0.06431379200148582, 0.640959, 0.116492, 0.602065, -0.06392169144058227, 0.645872, 0.120898, 0.598867, -0.06352949087953567, 0.650746, 0.125309, 0.595617, -0.06313739031863214, 0.65558, 0.129725, 0.592317, -0.06274518975758553, 0.660374, 0.134144, 0.588971, -0.06235298919653893, 0.665129, 0.138566, 0.585582, -0.061960888635635376, 0.669845, 0.142992, 0.582154, -0.061568688074588776, 0.674522, 0.147419, 0.578688, -0.061176587513685224, 0.67916, 0.151848, 0.575189, -0.06078438695263863, 0.683758, 0.156278, 0.57166, -0.06039228639173508, 0.688318, 0.160709, 0.568103, -0.06000008583068847, 0.69284, 0.165141, 0.564522, -0.05960788526964188, 0.697324, 0.169573, 0.560919, -0.059215784708738325, 0.701769, 0.174005, 0.557296, -0.058823584147691725, 0.706178, 0.178437, 0.553657, -0.05843148358678818, 0.710549, 0.182868, 0.550004, -0.05803928302574158, 0.714883, 0.187299, 0.546338, -0.05764718246483803, 0.719181, 0.191729, 0.542663, -0.05725498190379143, 0.723444, 0.196158, 0.538981, -0.05686278134274483, 0.72767, 0.200586, 0.535293, -0.056470680781841275, 0.731862, 0.205013, 0.531601, -0.05607848022079468, 0.736019, 0.209439, 0.527908, -0.05568637965989113, 0.740143, 0.213864, 0.524216, -0.05529417909884453, 0.744232, 0.218288, 0.520524, -0.054902078537940976, 0.748289, 0.222711, 0.516834, -0.05450987797689438, 0.752312, 0.227133, 0.513149, -0.054117677415847776, 0.756304, 0.231555, 0.509468, -0.05372557685494423, 0.760264, 0.235976, 0.505794, -0.05333337629389763, 0.764193, 0.240396, 0.502126, -0.05294127573299408, 0.76809, 0.244817, 0.498465, -0.05254907517194748, 0.771958, 0.249237, 0.494813, -0.05215697461104393, 0.775796, 0.253658, 0.491171, -0.05176477404999733, 0.779604, 0.258078, 0.487539, -0.051372573488950725, 0.783383, 0.2625, 0.483918, -0.05098047292804718, 0.787133, 0.266922, 0.480307, -0.05058827236700058, 0.790855, 0.271345, 0.476706, -0.05019617180609703, 0.794549, 0.27577, 0.473117, -0.049803971245050434, 0.798216, 0.280197, 0.469538, -0.049411870684146875, 0.801855, 0.284626, 0.465971, -0.049019670123100274, 0.805467, 0.289057, 0.462415, -0.048627569562196736, 0.809052, 0.293491, 0.45887, -0.048235369001150136, 0.812612, 0.297928, 0.455338, -0.047843168440103535, 0.816144, 0.302368, 0.451816, -0.04745106787919998, 0.819651, 0.306812, 0.448306, -0.04705886731815338, 0.823132, 0.311261, 0.444806, -0.04666676675724984, 0.826588, 0.315714, 0.441316, -0.04627456619620323, 0.830018, 0.320172, 0.437836, -0.045882465635299685, 0.833422, 0.324635, 0.434366, -0.045490265074253085, 0.836801, 0.329105, 0.430905, -0.045098064513206484, 0.840155, 0.33358, 0.427455, -0.04470596395230293, 0.843484, 0.338062, 0.424013, -0.04431376339125633, 0.846788, 0.342551, 0.420579, -0.04392166283035279, 0.850066, 0.347048, 0.417153, -0.04352946226930618, 0.853319, 0.351553, 0.413734, -0.043137361708402634, 0.856547, 0.356066, 0.410322, -0.042745161147356034, 0.85975, 0.360588, 0.406917, -0.04235296058630944, 0.862927, 0.365119, 0.403519, -0.04196086002540588, 0.866078, 0.36966, 0.400126, -0.04156865946435928, 0.869203, 0.374212, 0.396738, -0.041176558903455736, 0.872303, 0.378774, 0.393355, -0.04078435834240913, 0.875376, 0.383347, 0.389976, -0.04039225778150558, 0.878423, 0.387932, 0.3866, -0.04000005722045899, 0.881443, 0.392529, 0.383229, -0.03960785665941239, 0.884436, 0.397139, 0.37986, -0.03921575609850883, 0.887402, 0.401762, 0.376494, -0.03882355553746224, 0.89034, 0.406398, 0.37313, -0.03843145497655869, 0.89325, 0.411048, 0.369768, -0.03803925441551208, 0.896131, 0.415712, 0.366407, -0.03764715385460853, 0.898984, 0.420392, 0.363047, -0.03725495329356193, 0.901807, 0.425087, 0.359688, -0.03686275273251534, 0.904601, 0.429797, 0.356329, -0.036470652171611787, 0.907365, 0.434524, 0.35297, -0.03607845161056518, 0.910098, 0.439268, 0.34961, -0.03568635104966164, 0.9128, 0.444029, 0.346251, -0.035294150488615034, 0.915471, 0.448807, 0.34289, -0.03490204992771148, 0.918109, 0.453603, 0.339529, -0.03450984936666489, 0.920714, 0.458417, 0.336166, -0.034117648805618295, 0.923287, 0.463251, 0.332801, -0.03372554824471473, 0.925825, 0.468103, 0.329435, -0.033333347683668135, 0.928329, 0.472975, 0.326067, -0.0329412471227646, 0.930798, 0.477867, 0.322697, -0.032549046561717976, 0.933232, 0.48278, 0.319325, -0.03215694600081444, 0.93563, 0.487712, 0.315952, -0.031764745439767844, 0.93799, 0.492667, 0.312575, -0.03137254487872124, 0.940313, 0.497642, 0.309197, -0.030980444317817685, 0.942598, 0.502639, 0.305816, -0.03058824375677109, 0.944844, 0.507658, 0.302433, -0.03019614319586754, 0.947051, 0.512699, 0.299049, -0.029803942634820946, 0.949217, 0.517763, 0.295662, -0.029411842073917394, 0.951344, 0.52285, 0.292275, -0.029019641512870786, 0.953428, 0.52796, 0.288883, -0.028627540951967234, 0.95547, 0.533093, 0.28549, -0.02823534039092064, 0.957469, 0.53825, 0.282096, -0.027843139829874033, 0.959424, 0.543431, 0.278701, -0.027451039268970495, 0.961336, 0.548636, 0.275305, -0.027058838707923888, 0.963203, 0.553865, 0.271909, -0.026666738147020336, 0.965024, 0.559118, 0.268513, -0.026274537585973742, 0.966798, 0.564396, 0.265118, -0.02588243702507019, 0.968526, 0.5697, 0.261721, -0.025490236464023583, 0.970205, 0.575028, 0.258325, -0.02509803590297699, 0.971835, 0.580382, 0.254931, -0.024705935342073437, 0.973416, 0.585761, 0.25154, -0.024313734781026844, 0.974947, 0.591165, 0.248151, -0.023921634220123292, 0.976428, 0.596595, 0.244767, -0.023529433659076684, 0.977856, 0.602051, 0.241387, -0.023137333098173146, 0.979233, 0.607532, 0.238013, -0.02274513253712654, 0.980556, 0.613039, 0.234646, -0.02235293197607993, 0.981826, 0.618572, 0.231287, -0.021960831415176393, 0.983041, 0.624131, 0.227937, -0.0215686308541298, 0.984199, 0.629718, 0.224595, -0.021176530293226234, 0.985301, 0.63533, 0.221265, -0.02078432973217964, 0.986345, 0.640969, 0.217948, -0.020392229171276102, 0.987332, 0.646633, 0.214648, -0.02000002861022948, 0.98826, 0.652325, 0.211364, -0.019607828049182888, 0.989128, 0.658043, 0.2081, -0.01921572748827935, 0.989935, 0.663787, 0.204859, -0.018823526927232742, 0.990681, 0.669558, 0.201642, -0.01843142636632919, 0.991365, 0.675355, 0.198453, -0.018039225805282597, 0.991985, 0.681179, 0.195295, -0.017647125244379044, 0.992541, 0.68703, 0.19217, -0.017254924683332437, 0.993032, 0.692907, 0.189084, -0.016862724122285844, 0.993456, 0.69881, 0.186041, -0.01647062356138229, 0.993814, 0.704741, 0.183043, -0.016078423000335698, 0.994103, 0.710698, 0.180097, -0.015686322439432146, 0.994324, 0.716681, 0.177208, -0.015294121878385539, 0.994474, 0.722691, 0.174381, -0.014902021317482, 0.994553, 0.728728, 0.171622, -0.014509820756435393, 0.994561, 0.734791, 0.168938, -0.014117620195388786, 0.994495, 0.74088, 0.166335, -0.013725519634485248, 0.994355, 0.746995, 0.163821, -0.013333319073438654, 0.994141, 0.753137, 0.161404, -0.012941218512535088, 0.993851, 0.759304, 0.159092, -0.012549017951488495, 0.993482, 0.765499, 0.156891, -0.012156917390584943, 0.993033, 0.77172, 0.154808, -0.011764716829538335, 0.992505, 0.777967, 0.152855, -0.011372516268491742, 0.991897, 0.784239, 0.151042, -0.010980415707588204, 0.991209, 0.790537, 0.149377, -0.010588215146541596, 0.990439, 0.796859, 0.14787, -0.010196114585638044, 0.989587, 0.803205, 0.146529, -0.00980391402459145, 0.988648, 0.809579, 0.145357, -0.009411813463687899, 0.987621, 0.815978, 0.144363, -0.009019612902641305, 0.986509, 0.822401, 0.143557, -0.008627512341737753, 0.985314, 0.828846, 0.142945, -0.008235311780691146, 0.984031, 0.835315, 0.142528, -0.007843111219644552, 0.982653, 0.841812, 0.142303, -0.007451010658741, 0.98119, 0.848329, 0.142279, -0.007058810097694393, 0.979644, 0.854866, 0.142453, -0.006666709536790855, 0.977995, 0.861432, 0.142808, -0.006274508975744247, 0.976265, 0.868016, 0.143351, -0.005882408414840695, 0.974443, 0.874622, 0.144061, -0.005490207853794102, 0.97253, 0.88125, 0.144923, -0.0050980072927474945, 0.970533, 0.887896, 0.145919, -0.004705906731843942, 0.968443, 0.894564, 0.147014, -0.004313706170797349, 0.966271, 0.901249, 0.14818, -0.003921605609893797, 0.964021, 0.90795, 0.14937, -0.0035294050488472034, 0.961681, 0.914672, 0.15052, -0.0031373044879436512, 0.959276, 0.921407, 0.151566, -0.002745103926897044, 0.956808, 0.928152, 0.152409, -0.0023529033658504506, 0.954287, 0.934908, 0.152921, -0.0019608028049468984, 0.951726, 0.941671, 0.152925, -0.0015686022439002911, 0.949151, 0.948435, 0.152178, -0.0011765016829967528, 0.946602, 0.95519, 0.150328, -0.0007843011219501594, 0.944152, 0.961916, 0.146861, -0.0003922005610465934, 0.941896, 0.96859, 0.140956, 0.0, 0.940015, 0.975158, 0.131326]
g_EQN_TRANSPORTLUT.NanColor = [0.0, 1.0, 0.0]
g_EQN_TRANSPORTLUT.NumberOfTableValues = 1
g_EQN_TRANSPORTLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.DiffuseColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.LookupTable = g_EQN_TRANSPORTLUT
contour1Display.InterpolateScalarsBeforeMapping = 0
contour1Display.Specular = 0.67
contour1Display.Luminosity = 35.0
contour1Display.Ambient = 0.24
contour1Display.Roughness = 0.22
contour1Display.RepeatTextures = 0
contour1Display.OSPRayScaleArray = 'G_EQN_TRANSPORT'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'G_EQN_TRANSPORT'
contour1Display.ScaleFactor = 4.941700026392937e-05
contour1Display.SelectScaleArray = 'G_EQN_TRANSPORT'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
contour1Display.GaussianRadius = 2.470850013196468e-06
contour1Display.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, -0.09998609125614166, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, -0.09998609125614166, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay = Show(exhaust_BackStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay.Representation = 'Surface'
exhaust_BackStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.ScaleFactor = 0.00973363183438778
exhaust_BackStreamTracerDisplay.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.GaussianRadius = 0.00048668159171938897
exhaust_BackStreamTracerDisplay.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay.ScaleTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay.OpacityTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay = Show(exhaust_BackArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay.Representation = 'Surface'
exhaust_BackArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay.ColorArrayName = ['POINTS', '']
exhaust_BackArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay.ScaleFactor = 0.010298835672438146
exhaust_BackArrowsDisplay.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.GaussianRadius = 0.0005149417836219073
exhaust_BackArrowsDisplay.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay.ScaleTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay.OpacityTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from intake_Geometry
intake_GeometryDisplay = Show(intake_Geometry, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay.Representation = 'Surface'
intake_GeometryDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay.ColorArrayName = ['POINTS', '']
intake_GeometryDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay.Opacity = 0.25
intake_GeometryDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay.SelectOrientationVectors = 'None'
intake_GeometryDisplay.ScaleFactor = 0.027035209536552432
intake_GeometryDisplay.SelectScaleArray = 'None'
intake_GeometryDisplay.GlyphType = 'Arrow'
intake_GeometryDisplay.GlyphTableIndexArray = 'None'
intake_GeometryDisplay.GaussianRadius = 0.0013517604768276215
intake_GeometryDisplay.SetScaleArray = [None, '']
intake_GeometryDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay.OpacityArray = [None, '']
intake_GeometryDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay.ScalarOpacityUnitDistance = 0.0023014537338361435
intake_GeometryDisplay.OpacityArrayName = [None, '']
intake_GeometryDisplay.ExtractedBlockIndex = 1

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

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.AutoOrient = 0
velocityLUTColorBar.WindowLocation = 'AnyLocation'
velocityLUTColorBar.Position = [0.005095541401273885, 0.03359173126614989]
velocityLUTColorBar.Title = 'Velocity'
velocityLUTColorBar.ComponentTitle = ''
velocityLUTColorBar.HorizontalTitle = 1
velocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.TitleFontSize = 12
velocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.LabelFontSize = 12
velocityLUTColorBar.UseCustomLabels = 1
velocityLUTColorBar.CustomLabels = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0]
velocityLUTColorBar.AddRangeLabels = 0
velocityLUTColorBar.ScalarBarThickness = 14
velocityLUTColorBar.ScalarBarLength = 0.5000000000000001

# set color bar visibility
velocityLUTColorBar.Visibility = 1

# show color legend
intake_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
intake_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_1 = Show(intake_Geometry, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_1.Representation = 'Surface'
intake_GeometryDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_1.ColorArrayName = [None, '']
intake_GeometryDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_1.Opacity = 0.25
intake_GeometryDisplay_1.SelectTCoordArray = 'None'
intake_GeometryDisplay_1.SelectNormalArray = 'None'
intake_GeometryDisplay_1.SelectTangentArray = 'None'
intake_GeometryDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.SelectOrientationVectors = 'None'
intake_GeometryDisplay_1.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_1.SelectScaleArray = 'None'
intake_GeometryDisplay_1.GlyphType = 'Arrow'
intake_GeometryDisplay_1.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_1.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_1.SetScaleArray = [None, '']
intake_GeometryDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.OpacityArray = [None, '']
intake_GeometryDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_1.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_1.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_1.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_GeometryDisplay_1.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_1 = Show(plug, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_1.Representation = 'Surface'
plugDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.ColorArrayName = [None, '']
plugDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.Opacity = 0.7
plugDisplay_1.SelectTCoordArray = 'None'
plugDisplay_1.SelectNormalArray = 'None'
plugDisplay_1.SelectTangentArray = 'None'
plugDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_1.SelectOrientationVectors = 'None'
plugDisplay_1.ScaleFactor = 0.00010781330056488515
plugDisplay_1.SelectScaleArray = 'None'
plugDisplay_1.GlyphType = 'Arrow'
plugDisplay_1.GlyphTableIndexArray = 'None'
plugDisplay_1.GaussianRadius = 5.390665028244257e-06
plugDisplay_1.SetScaleArray = [None, '']
plugDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_1.OpacityArray = [None, '']
plugDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_1.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_1.ScalarOpacityUnitDistance = 0.00016043032651082378
plugDisplay_1.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
plugDisplay_1.ExtractedBlockIndex = 1

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay_1 = Show(intakeExhaust_Geometry, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay_1.Representation = 'Surface'
intakeExhaust_GeometryDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay_1.ColorArrayName = ['POINTS', '']
intakeExhaust_GeometryDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay_1.Opacity = 0.25
intakeExhaust_GeometryDisplay_1.SelectTCoordArray = 'None'
intakeExhaust_GeometryDisplay_1.SelectNormalArray = 'None'
intakeExhaust_GeometryDisplay_1.SelectTangentArray = 'None'
intakeExhaust_GeometryDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay_1.ScaleFactor = 0.027035209536552432
intakeExhaust_GeometryDisplay_1.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay_1.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay_1.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay_1.GaussianRadius = 0.0013517604768276215
intakeExhaust_GeometryDisplay_1.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay_1.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay_1.ScalarOpacityUnitDistance = 0.0023014537338361435
intakeExhaust_GeometryDisplay_1.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intakeExhaust_GeometryDisplay_1.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_1 = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_1.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'None'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = -2.0000000000000002e+298
contour1Display_1.SelectScaleArray = 'None'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'None'
contour1Display_1.GaussianRadius = -1e+297
contour1Display_1.SetScaleArray = [None, '']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = [None, '']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'

# show data from parcel
parcelDisplay = Show(parcel, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'dp_TEMP'
dp_TEMPLUT = GetColorTransferFunction('dp_TEMP')
dp_TEMPLUT.AutomaticRescaleRangeMode = 'Never'
dp_TEMPLUT.RGBPoints = [200.0, 0.0, 0.0, 0.34902, 209.375, 0.039216, 0.062745, 0.380392, 218.75, 0.062745, 0.117647, 0.411765, 228.125, 0.090196, 0.184314, 0.45098, 237.5, 0.12549, 0.262745, 0.501961, 246.875, 0.160784, 0.337255, 0.541176, 256.25, 0.2, 0.396078, 0.568627, 265.625, 0.239216, 0.454902, 0.6, 275.0, 0.286275, 0.521569, 0.65098, 284.375, 0.337255, 0.592157, 0.701961, 293.75, 0.388235, 0.654902, 0.74902, 303.125, 0.466667, 0.737255, 0.819608, 312.5, 0.572549, 0.819608, 0.878431, 321.875, 0.654902, 0.866667, 0.909804, 331.25, 0.752941, 0.917647, 0.941176, 340.625, 0.823529, 0.956863, 0.968627, 350.0, 0.941176, 0.984314, 0.988235, 350.0, 0.988235, 0.960784, 0.901961, 356.0, 0.988235, 0.945098, 0.85098, 362.0, 0.980392, 0.898039, 0.784314, 368.75, 0.968627, 0.835294, 0.698039, 378.125, 0.94902, 0.733333, 0.588235, 387.5, 0.929412, 0.65098, 0.509804, 396.875, 0.909804, 0.564706, 0.435294, 406.25, 0.878431, 0.458824, 0.352941, 415.625, 0.839216, 0.388235, 0.286275, 425.0, 0.760784, 0.294118, 0.211765, 434.375, 0.701961, 0.211765, 0.168627, 443.75, 0.65098, 0.156863, 0.129412, 453.125, 0.6, 0.094118, 0.094118, 462.5, 0.54902, 0.066667, 0.098039, 471.875, 0.501961, 0.05098, 0.12549, 481.25, 0.45098, 0.054902, 0.172549, 490.625, 0.4, 0.054902, 0.192157, 500.0, 0.34902, 0.070588, 0.211765]
dp_TEMPLUT.ColorSpace = 'Lab'
dp_TEMPLUT.NanColor = [0.25, 0.0, 0.0]
dp_TEMPLUT.Discretize = 0
dp_TEMPLUT.NumberOfTableValues = 7
dp_TEMPLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'dp_TEMP'
dp_TEMPPWF = GetOpacityTransferFunction('dp_TEMP')
dp_TEMPPWF.Points = [200.0, 0.0, 0.5, 0.0, 500.0, 1.0, 0.5, 0.0]
dp_TEMPPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
parcelDisplay.Representation = 'Surface'
parcelDisplay.ColorArrayName = ['POINTS', 'dp_TEMP']
parcelDisplay.LookupTable = dp_TEMPLUT
parcelDisplay.SelectTCoordArray = 'None'
parcelDisplay.SelectNormalArray = 'None'
parcelDisplay.SelectTangentArray = 'None'
parcelDisplay.OSPRayScaleArray = 'dp_TEMP'
parcelDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay.SelectOrientationVectors = 'None'
parcelDisplay.ScaleFactor = 0.015194140002131463
parcelDisplay.SelectScaleArray = 'None'
parcelDisplay.GlyphType = 'Arrow'
parcelDisplay.GlyphTableIndexArray = 'None'
parcelDisplay.GaussianRadius = 0.0007597070001065732
parcelDisplay.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay.ScalarOpacityFunction = dp_TEMPPWF
parcelDisplay.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay.OpacityArrayName = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
parcelDisplay.OSPRayScaleFunction.Points = [0.01, 0.0, 0.5, 0.0, 0.012375690555555556, 0.6145833134651184, 0.5, 0.0, 0.016160221111111112, 0.8333333134651184, 0.5, 0.0, 0.02, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for dp_TEMPLUT in view renderView2
dp_TEMPLUTColorBar = GetScalarBar(dp_TEMPLUT, renderView2)
dp_TEMPLUTColorBar.WindowLocation = 'LowerLeftCorner'
dp_TEMPLUTColorBar.Position = [0.8525754884547069, 0.088]
dp_TEMPLUTColorBar.Title = 'Parcel Temp'
dp_TEMPLUTColorBar.ComponentTitle = ''
dp_TEMPLUTColorBar.HorizontalTitle = 1
dp_TEMPLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar.AddRangeLabels = 0
dp_TEMPLUTColorBar.ScalarBarLength = 0.5

# set color bar visibility
dp_TEMPLUTColorBar.Visibility = 1

# show color legend
parcelDisplay.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_2 = Show(intake_Geometry, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_2.Representation = 'Surface'
intake_GeometryDisplay_2.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_2.ColorArrayName = [None, '']
intake_GeometryDisplay_2.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_2.Opacity = 0.25
intake_GeometryDisplay_2.SelectTCoordArray = 'None'
intake_GeometryDisplay_2.SelectNormalArray = 'None'
intake_GeometryDisplay_2.SelectTangentArray = 'None'
intake_GeometryDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.SelectOrientationVectors = 'None'
intake_GeometryDisplay_2.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_2.SelectScaleArray = 'None'
intake_GeometryDisplay_2.GlyphType = 'Arrow'
intake_GeometryDisplay_2.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_2.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_2.SetScaleArray = [None, '']
intake_GeometryDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.OpacityArray = [None, '']
intake_GeometryDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_2.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_2.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_2.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_GeometryDisplay_2.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_2 = Show(plug, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_2.Representation = 'Surface'
plugDisplay_2.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_2.ColorArrayName = [None, '']
plugDisplay_2.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_2.Opacity = 0.7
plugDisplay_2.SelectTCoordArray = 'None'
plugDisplay_2.SelectNormalArray = 'None'
plugDisplay_2.SelectTangentArray = 'None'
plugDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_2.SelectOrientationVectors = 'None'
plugDisplay_2.ScaleFactor = 0.0010427969042211772
plugDisplay_2.SelectScaleArray = 'None'
plugDisplay_2.GlyphType = 'Arrow'
plugDisplay_2.GlyphTableIndexArray = 'None'
plugDisplay_2.GaussianRadius = 5.2139845211058853e-05
plugDisplay_2.SetScaleArray = [None, '']
plugDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_2.OpacityArray = [None, '']
plugDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_2.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_2.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_2.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
plugDisplay_2.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_1 = Show(intake_FrontStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_1.Representation = 'Surface'
intake_FrontStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_1.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_1.SelectTCoordArray = 'None'
intake_FrontStreamTracerDisplay_1.SelectNormalArray = 'None'
intake_FrontStreamTracerDisplay_1.SelectTangentArray = 'None'
intake_FrontStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.ScaleFactor = 0.014265598356723787
intake_FrontStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.GaussianRadius = 0.0007132799178361893
intake_FrontStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# show data from intake_FrontArrows
intake_FrontArrowsDisplay_1 = Show(intake_FrontArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay_1.Representation = 'Surface'
intake_FrontArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_1.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_1.SelectTCoordArray = 'None'
intake_FrontArrowsDisplay_1.SelectNormalArray = 'None'
intake_FrontArrowsDisplay_1.SelectTangentArray = 'None'
intake_FrontArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_FrontArrowsDisplay_1.ScaleFactor = 0.014322103932499886
intake_FrontArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.GlyphType = 'Arrow'
intake_FrontArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.GaussianRadius = 0.0007161051966249943
intake_FrontArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay_1.ScaleTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay_1.OpacityTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay_1 = Show(intake_BackStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay_1.Representation = 'Surface'
intake_BackStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay_1.LookupTable = velocityLUT
intake_BackStreamTracerDisplay_1.SelectTCoordArray = 'None'
intake_BackStreamTracerDisplay_1.SelectNormalArray = 'None'
intake_BackStreamTracerDisplay_1.SelectTangentArray = 'None'
intake_BackStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.ScaleFactor = 0.014364903420209886
intake_BackStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.GaussianRadius = 0.0007182451710104942
intake_BackStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# show data from intake_BackArrows
intake_BackArrowsDisplay_1 = Show(intake_BackArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay_1.Representation = 'Surface'
intake_BackArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_1.ColorArrayName = [None, '']
intake_BackArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_1.SelectTCoordArray = 'None'
intake_BackArrowsDisplay_1.SelectNormalArray = 'None'
intake_BackArrowsDisplay_1.SelectTangentArray = 'None'
intake_BackArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_BackArrowsDisplay_1.ScaleFactor = 0.014297069981694221
intake_BackArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.GlyphType = 'Arrow'
intake_BackArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.GaussianRadius = 0.000714853499084711
intake_BackArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay_1.ScaleTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay_1.OpacityTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay_1 = Show(exhaust_FrontStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay_1.Representation = 'Surface'
exhaust_FrontStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay_1.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay_1.SelectTCoordArray = 'None'
exhaust_FrontStreamTracerDisplay_1.SelectNormalArray = 'None'
exhaust_FrontStreamTracerDisplay_1.SelectTangentArray = 'None'
exhaust_FrontStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.ScaleFactor = 0.014060626551508904
exhaust_FrontStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.GaussianRadius = 0.0007030313275754452
exhaust_FrontStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay_1 = Show(exhaust_FrontArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay_1.Representation = 'Surface'
exhaust_FrontArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_1.ColorArrayName = [None, '']
exhaust_FrontArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_1.SelectTCoordArray = 'None'
exhaust_FrontArrowsDisplay_1.SelectNormalArray = 'None'
exhaust_FrontArrowsDisplay_1.SelectTangentArray = 'None'
exhaust_FrontArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.ScaleFactor = 0.014079396799206735
exhaust_FrontArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.GaussianRadius = 0.0007039698399603367
exhaust_FrontArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay_1.ScaleTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay_1.OpacityTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay_1 = Show(exhaust_BackStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay_1.Representation = 'Surface'
exhaust_BackStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay_1.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay_1.SelectTCoordArray = 'None'
exhaust_BackStreamTracerDisplay_1.SelectNormalArray = 'None'
exhaust_BackStreamTracerDisplay_1.SelectTangentArray = 'None'
exhaust_BackStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.ScaleFactor = 0.014190616831183434
exhaust_BackStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.GaussianRadius = 0.0007095308415591717
exhaust_BackStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay_1 = Show(exhaust_BackArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay_1.Representation = 'Surface'
exhaust_BackArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_1.ColorArrayName = [None, '']
exhaust_BackArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_1.SelectTCoordArray = 'None'
exhaust_BackArrowsDisplay_1.SelectNormalArray = 'None'
exhaust_BackArrowsDisplay_1.SelectTangentArray = 'None'
exhaust_BackArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.ScaleFactor = 0.014254055917263031
exhaust_BackArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.GaussianRadius = 0.0007127027958631516
exhaust_BackArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay_1.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay_1.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_2 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'None'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = -2.0000000000000002e+298
contour1Display_2.SelectScaleArray = 'None'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'None'
contour1Display_2.GaussianRadius = -1e+297
contour1Display_2.SetScaleArray = [None, '']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = [None, '']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'

# show data from head
headDisplay = Show(head, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay.Representation = 'Surface'
headDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay.ColorArrayName = [None, '']
headDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay.Opacity = 0.25
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
headDisplay.ScalarOpacityUnitDistance = 0.0016640944230168922
headDisplay.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
headDisplay.ExtractedBlockIndex = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_3 = Show(intake_Geometry, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_3.Representation = 'Surface'
intake_GeometryDisplay_3.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_3.ColorArrayName = [None, '']
intake_GeometryDisplay_3.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_3.Opacity = 0.25
intake_GeometryDisplay_3.SelectTCoordArray = 'None'
intake_GeometryDisplay_3.SelectNormalArray = 'None'
intake_GeometryDisplay_3.SelectTangentArray = 'None'
intake_GeometryDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.SelectOrientationVectors = 'None'
intake_GeometryDisplay_3.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_3.SelectScaleArray = 'None'
intake_GeometryDisplay_3.GlyphType = 'Arrow'
intake_GeometryDisplay_3.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_3.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_3.SetScaleArray = [None, '']
intake_GeometryDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.OpacityArray = [None, '']
intake_GeometryDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_3.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_3.ScalarOpacityUnitDistance = 0.0021597388225030813
intake_GeometryDisplay_3.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_GeometryDisplay_3.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_3 = Show(plug, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_3.Representation = 'Surface'
plugDisplay_3.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_3.ColorArrayName = [None, '']
plugDisplay_3.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_3.Opacity = 0.7
plugDisplay_3.SelectTCoordArray = 'None'
plugDisplay_3.SelectNormalArray = 'None'
plugDisplay_3.SelectTangentArray = 'None'
plugDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_3.SelectOrientationVectors = 'None'
plugDisplay_3.ScaleFactor = 0.0010427969042211772
plugDisplay_3.SelectScaleArray = 'None'
plugDisplay_3.GlyphType = 'Arrow'
plugDisplay_3.GlyphTableIndexArray = 'None'
plugDisplay_3.GaussianRadius = 5.2139845211058853e-05
plugDisplay_3.SetScaleArray = [None, '']
plugDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_3.OpacityArray = [None, '']
plugDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_3.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_3.ScalarOpacityUnitDistance = 0.0004946801360981299
plugDisplay_3.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
plugDisplay_3.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_2 = Show(intake_FrontStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_2.Representation = 'Surface'
intake_FrontStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_2.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_2.SelectTCoordArray = 'None'
intake_FrontStreamTracerDisplay_2.SelectNormalArray = 'None'
intake_FrontStreamTracerDisplay_2.SelectTangentArray = 'None'
intake_FrontStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.ScaleFactor = 0.014265598356723787
intake_FrontStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.GaussianRadius = 0.0007132799178361893
intake_FrontStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# show data from intake_FrontArrows
intake_FrontArrowsDisplay_2 = Show(intake_FrontArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay_2.Representation = 'Surface'
intake_FrontArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_2.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_2.SelectTCoordArray = 'None'
intake_FrontArrowsDisplay_2.SelectNormalArray = 'None'
intake_FrontArrowsDisplay_2.SelectTangentArray = 'None'
intake_FrontArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_FrontArrowsDisplay_2.ScaleFactor = 0.014322103932499886
intake_FrontArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.GlyphType = 'Arrow'
intake_FrontArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.GaussianRadius = 0.0007161051966249943
intake_FrontArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay_2.ScaleTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay_2.OpacityTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay_2 = Show(intake_BackStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay_2.Representation = 'Surface'
intake_BackStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay_2.LookupTable = velocityLUT
intake_BackStreamTracerDisplay_2.SelectTCoordArray = 'None'
intake_BackStreamTracerDisplay_2.SelectNormalArray = 'None'
intake_BackStreamTracerDisplay_2.SelectTangentArray = 'None'
intake_BackStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.ScaleFactor = 0.014364903420209886
intake_BackStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.GaussianRadius = 0.0007182451710104942
intake_BackStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# show data from intake_BackArrows
intake_BackArrowsDisplay_2 = Show(intake_BackArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay_2.Representation = 'Surface'
intake_BackArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_2.ColorArrayName = [None, '']
intake_BackArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_2.SelectTCoordArray = 'None'
intake_BackArrowsDisplay_2.SelectNormalArray = 'None'
intake_BackArrowsDisplay_2.SelectTangentArray = 'None'
intake_BackArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_BackArrowsDisplay_2.ScaleFactor = 0.014297069981694221
intake_BackArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.GlyphType = 'Arrow'
intake_BackArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.GaussianRadius = 0.000714853499084711
intake_BackArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay_2.ScaleTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay_2.OpacityTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay_2 = Show(exhaust_FrontStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay_2.Representation = 'Surface'
exhaust_FrontStreamTracerDisplay_2.AmbientColor = [0.0, 0.0, 0.0]
exhaust_FrontStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay_2.DiffuseColor = [0.0, 0.0, 0.0]
exhaust_FrontStreamTracerDisplay_2.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay_2.SelectTCoordArray = 'None'
exhaust_FrontStreamTracerDisplay_2.SelectNormalArray = 'None'
exhaust_FrontStreamTracerDisplay_2.SelectTangentArray = 'None'
exhaust_FrontStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.ScaleFactor = 0.014060626551508904
exhaust_FrontStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.GaussianRadius = 0.0007030313275754452
exhaust_FrontStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay_2 = Show(exhaust_FrontArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay_2.Representation = 'Surface'
exhaust_FrontArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_2.ColorArrayName = [None, '']
exhaust_FrontArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_2.SelectTCoordArray = 'None'
exhaust_FrontArrowsDisplay_2.SelectNormalArray = 'None'
exhaust_FrontArrowsDisplay_2.SelectTangentArray = 'None'
exhaust_FrontArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.ScaleFactor = 0.014079396799206735
exhaust_FrontArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.GaussianRadius = 0.0007039698399603367
exhaust_FrontArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay_2.ScaleTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay_2.OpacityTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay_2 = Show(exhaust_BackStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay_2.Representation = 'Surface'
exhaust_BackStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay_2.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay_2.SelectTCoordArray = 'None'
exhaust_BackStreamTracerDisplay_2.SelectNormalArray = 'None'
exhaust_BackStreamTracerDisplay_2.SelectTangentArray = 'None'
exhaust_BackStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.ScaleFactor = 0.014190616831183434
exhaust_BackStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.GaussianRadius = 0.0007095308415591717
exhaust_BackStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay_2 = Show(exhaust_BackArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay_2.Representation = 'Surface'
exhaust_BackArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_2.ColorArrayName = [None, '']
exhaust_BackArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_2.SelectTCoordArray = 'None'
exhaust_BackArrowsDisplay_2.SelectNormalArray = 'None'
exhaust_BackArrowsDisplay_2.SelectTangentArray = 'None'
exhaust_BackArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.ScaleFactor = 0.014254055917263031
exhaust_BackArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.GaussianRadius = 0.0007127027958631516
exhaust_BackArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay_2.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay_2.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_3 = Show(contour1, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_3.Representation = 'Surface'
contour1Display_3.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_3.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_3.SelectTCoordArray = 'None'
contour1Display_3.SelectNormalArray = 'None'
contour1Display_3.SelectTangentArray = 'None'
contour1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_3.SelectOrientationVectors = 'None'
contour1Display_3.ScaleFactor = -2.0000000000000002e+298
contour1Display_3.SelectScaleArray = 'None'
contour1Display_3.GlyphType = 'Arrow'
contour1Display_3.GlyphTableIndexArray = 'None'
contour1Display_3.GaussianRadius = -1e+297
contour1Display_3.SetScaleArray = [None, '']
contour1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_3.OpacityArray = [None, '']
contour1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_3.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_3.PolarAxes = 'PolarAxesRepresentation'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_4 = Show(intake_Geometry, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_4.Representation = 'Surface'
intake_GeometryDisplay_4.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_4.ColorArrayName = [None, '']
intake_GeometryDisplay_4.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_4.Opacity = 0.25
intake_GeometryDisplay_4.SelectTCoordArray = 'None'
intake_GeometryDisplay_4.SelectNormalArray = 'None'
intake_GeometryDisplay_4.SelectTangentArray = 'None'
intake_GeometryDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.SelectOrientationVectors = 'None'
intake_GeometryDisplay_4.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_4.SelectScaleArray = 'None'
intake_GeometryDisplay_4.GlyphType = 'Arrow'
intake_GeometryDisplay_4.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_4.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_4.SetScaleArray = [None, '']
intake_GeometryDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.OpacityArray = [None, '']
intake_GeometryDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_4.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_4.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_4.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_GeometryDisplay_4.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_4 = Show(plug, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_4.Representation = 'Surface'
plugDisplay_4.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_4.ColorArrayName = [None, '']
plugDisplay_4.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_4.Opacity = 0.7
plugDisplay_4.SelectTCoordArray = 'None'
plugDisplay_4.SelectNormalArray = 'None'
plugDisplay_4.SelectTangentArray = 'None'
plugDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_4.SelectOrientationVectors = 'None'
plugDisplay_4.ScaleFactor = 0.0010427969042211772
plugDisplay_4.SelectScaleArray = 'None'
plugDisplay_4.GlyphType = 'Arrow'
plugDisplay_4.GlyphTableIndexArray = 'None'
plugDisplay_4.GaussianRadius = 5.2139845211058853e-05
plugDisplay_4.SetScaleArray = [None, '']
plugDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_4.OpacityArray = [None, '']
plugDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_4.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_4.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_4.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
plugDisplay_4.ExtractedBlockIndex = 1

# show data from head
headDisplay_1 = Show(head, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay_1.Representation = 'Surface'
headDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_1.ColorArrayName = [None, '']
headDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_1.Opacity = 0.25
headDisplay_1.SelectTCoordArray = 'None'
headDisplay_1.SelectNormalArray = 'None'
headDisplay_1.SelectTangentArray = 'None'
headDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
headDisplay_1.SelectOrientationVectors = 'None'
headDisplay_1.ScaleFactor = 0.008899322897195817
headDisplay_1.SelectScaleArray = 'None'
headDisplay_1.GlyphType = 'Arrow'
headDisplay_1.GlyphTableIndexArray = 'None'
headDisplay_1.GaussianRadius = 0.0004449661448597908
headDisplay_1.SetScaleArray = [None, '']
headDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
headDisplay_1.OpacityArray = [None, '']
headDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
headDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
headDisplay_1.PolarAxes = 'PolarAxesRepresentation'
headDisplay_1.ScalarOpacityUnitDistance = 0.0016640944230168922
headDisplay_1.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
headDisplay_1.ExtractedBlockIndex = 1

# show data from parcel
parcelDisplay_1 = Show(parcel, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
parcelDisplay_1.Representation = 'Surface'
parcelDisplay_1.ColorArrayName = ['POINTS', 'dp_TEMP']
parcelDisplay_1.LookupTable = dp_TEMPLUT
parcelDisplay_1.SelectTCoordArray = 'None'
parcelDisplay_1.SelectNormalArray = 'None'
parcelDisplay_1.SelectTangentArray = 'None'
parcelDisplay_1.OSPRayScaleArray = 'dp_FROM_NOZZLE'
parcelDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay_1.SelectOrientationVectors = 'None'
parcelDisplay_1.ScaleFactor = 0.015194140002131463
parcelDisplay_1.SelectScaleArray = 'None'
parcelDisplay_1.GlyphType = 'Arrow'
parcelDisplay_1.GlyphTableIndexArray = 'None'
parcelDisplay_1.GaussianRadius = 0.0007597070001065732
parcelDisplay_1.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay_1.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay_1.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay_1.ScalarOpacityFunction = dp_TEMPPWF
parcelDisplay_1.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay_1.OpacityArrayName = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_1.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_4 = Show(contour1, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_4.Representation = 'Surface'
contour1Display_4.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_4.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_4.SelectTCoordArray = 'None'
contour1Display_4.SelectNormalArray = 'None'
contour1Display_4.SelectTangentArray = 'None'
contour1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_4.SelectOrientationVectors = 'None'
contour1Display_4.ScaleFactor = -2.0000000000000002e+298
contour1Display_4.SelectScaleArray = 'None'
contour1Display_4.GlyphType = 'Arrow'
contour1Display_4.GlyphTableIndexArray = 'None'
contour1Display_4.GaussianRadius = -1e+297
contour1Display_4.SetScaleArray = [None, '']
contour1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_4.OpacityArray = [None, '']
contour1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_4.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_4.PolarAxes = 'PolarAxesRepresentation'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView6'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_5 = Show(intake_Geometry, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_5.Representation = 'Surface'
intake_GeometryDisplay_5.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_5.ColorArrayName = [None, '']
intake_GeometryDisplay_5.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_5.Opacity = 0.25
intake_GeometryDisplay_5.SelectTCoordArray = 'None'
intake_GeometryDisplay_5.SelectNormalArray = 'None'
intake_GeometryDisplay_5.SelectTangentArray = 'None'
intake_GeometryDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.SelectOrientationVectors = 'None'
intake_GeometryDisplay_5.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_5.SelectScaleArray = 'None'
intake_GeometryDisplay_5.GlyphType = 'Arrow'
intake_GeometryDisplay_5.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_5.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_5.SetScaleArray = [None, '']
intake_GeometryDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.OpacityArray = [None, '']
intake_GeometryDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_5.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_5.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_5.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
intake_GeometryDisplay_5.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_5 = Show(plug, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_5.Representation = 'Surface'
plugDisplay_5.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_5.ColorArrayName = [None, '']
plugDisplay_5.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_5.Opacity = 0.7
plugDisplay_5.SelectTCoordArray = 'None'
plugDisplay_5.SelectNormalArray = 'None'
plugDisplay_5.SelectTangentArray = 'None'
plugDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_5.SelectOrientationVectors = 'None'
plugDisplay_5.ScaleFactor = 0.0010427969042211772
plugDisplay_5.SelectScaleArray = 'None'
plugDisplay_5.GlyphType = 'Arrow'
plugDisplay_5.GlyphTableIndexArray = 'None'
plugDisplay_5.GaussianRadius = 5.2139845211058853e-05
plugDisplay_5.SetScaleArray = [None, '']
plugDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_5.OpacityArray = [None, '']
plugDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_5.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_5.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_5.OpacityArrayName = ['CELLS', 'G_EQN_TRANSPORT']
plugDisplay_5.ExtractedBlockIndex = 1

# show data from parcel
parcelDisplay_2 = Show(parcel, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
parcelDisplay_2.Representation = 'Surface'
parcelDisplay_2.ColorArrayName = ['POINTS', 'dp_TEMP']
parcelDisplay_2.LookupTable = dp_TEMPLUT
parcelDisplay_2.SelectTCoordArray = 'None'
parcelDisplay_2.SelectNormalArray = 'None'
parcelDisplay_2.SelectTangentArray = 'None'
parcelDisplay_2.OSPRayScaleArray = 'dp_FROM_NOZZLE'
parcelDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay_2.SelectOrientationVectors = 'None'
parcelDisplay_2.ScaleFactor = 0.015194140002131463
parcelDisplay_2.SelectScaleArray = 'None'
parcelDisplay_2.GlyphType = 'Arrow'
parcelDisplay_2.GlyphTableIndexArray = 'None'
parcelDisplay_2.GaussianRadius = 0.0007597070001065732
parcelDisplay_2.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay_2.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay_2.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay_2.ScalarOpacityFunction = dp_TEMPPWF
parcelDisplay_2.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay_2.OpacityArrayName = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_2.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_5 = Show(contour1, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_5.Representation = 'Surface'
contour1Display_5.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_5.SelectTCoordArray = 'None'
contour1Display_5.SelectNormalArray = 'Normals'
contour1Display_5.SelectTangentArray = 'None'
contour1Display_5.OSPRayScaleArray = 'G_EQN_TRANSPORT'
contour1Display_5.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_5.SelectOrientationVectors = 'G_EQN_TRANSPORT'
contour1Display_5.ScaleFactor = 0.0025496815331280233
contour1Display_5.SelectScaleArray = 'G_EQN_TRANSPORT'
contour1Display_5.GlyphType = 'Arrow'
contour1Display_5.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
contour1Display_5.GaussianRadius = 0.00012748407665640117
contour1Display_5.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_5.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_5.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_5.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_5.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_5.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTPWF = GetOpacityTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTPWF.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
g_EQN_TRANSPORTPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.0, 0.0, 0.5, 0.0, 150.0, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(intake_FrontArrows)
# ----------------------------------------------------------------

SaveScreenshot(filename, layout1)
